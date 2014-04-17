# all the imports
import sys
from flask import session, redirect, url_for, render_template, flash, request, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user
from ops import app, facebook, twitter, mongo
from auth import User
import time
from mock_data import jobs_data, items
import db


@app.route('/')
def show_landing():
    if current_user.is_authenticated():
        username = current_user.username
    else:
        username = None
    return render_template('landing.html', showbg=True)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('home', username=current_user.username))
    if request.method == 'POST':
        stored_user = mongo.db.participants.find_one({'username': request.form['username']})
        print stored_user
        if stored_user:
            user = User(username=stored_user['username'], name=stored_user['name'])
            print user.name
            print user.username
            user.load_participant(stored_user)
            print "user loaded"
            login_user(user)
            print "user logged in"
            return redirect(url_for('home', username=user.username))
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_landing'))


@app.route('/progress')
def progress():
    return jsonify(prog=time.time() % 50 * 2, jobs=jobs_data)


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated():
        return redirect(url_for('home'))
    if request.method == 'POST':
        user = User(request.form['username'], request.form['name'])
        mongo.db.participants.insert(user.save_participant())
        login_user(user)
        return redirect(url_for('home', username=user.username))
    return render_template('signup.html')


@app.route('/docs')
def docs():
    return 'Docs'


@app.route('/fetchitems', methods=['POST'])
def fetch_items():
    item_type = request.form.get('item_type')
    pane_id = request.form.get('pane_id')

    return render_template('items.html', item_type=item_type, items=find_items_by_type(item_type), pane_id=pane_id)


def find_items_by_type(self, item_type):
    item_map = {}
    item_map['friends'] = lambda: db.find_participants({})
    return item_map[item_type]()


@app.route('/iteminfo', methods=['POST'])
def item_info():
    item_id = request.form['item_id']
    item_type = request.form['item_type']
    for item in items[item_type]:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify(None)


@app.route('/deleteitem', methods=['POST'])
def delete_item():
    item_id = request.form['item_id']
    item_type = request.form['item_type']
    pane_id = request.form['pane_id']
    # This will be much simpler with a call to the database using the item id.
    for item in items[item_type]:
        if item['id'] == int(item_id):
            item['visible'] = False
            break
    print items[item_type]
    return render_template('items.html', items=items[item_type], pane_id=pane_id, item_type=item_type)


@app.route('/jobs/<username>')
@login_required
def jobs(username):
    return render_template('jobs.html', jobs=jobs_data)


@app.route('/home/<username>')
@login_required
def home(username):
    return render_template('home.html', username=username)


@app.route('/settings/<username>')
@login_required
def settings(username):
    return render_template('settings.html', username=username)


@app.route('/friends/<username>')
@login_required
def friends(username):
    return render_template('friends.html', name=current_user.name)


@app.route('/request_friend/<friend_username>')
@login_required
def request_friend(friend_username):
    db.Request(current_user.username, friend_username).insert()


@app.route('/facebook')
def facebook_login():
    callback_url = url_for('facebook_auth', next=request.args.get('next'))
    return facebook.authorize(callback=callback_url)


@app.route('/facebook_auth')
@facebook.authorized_handler
def facebook_auth(resp):
    if resp is None:
        flash('You denied the request to sign in.')
        return redirect(request.args.get('next') or url_for('show_landing'))

    user = User(username=resp['screen_name'], name=resp['screen_name'],
                token=resp['oauth_token'], secret=resp['oauth_token_secret'])
    login_user(user)
    user.user_id = session['user_id']
    users.append(user)
    mongo.db.participants.insert(user.save_participant())
    return redirect(request.args.get('next') or url_for('home', username=user.username))


@app.route('/twitter')
def twitter_login():
    callback_url = url_for('twitter_auth', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url)


@app.route('/twitter_auth')
@twitter.authorized_handler
def twitter_auth(resp):
    if resp is None:
        flash('You denied the request to sign in.')
        return redirect(request.args.get('next') or url_for('show_landing'))

    user = User(username=resp['screen_name'], name=resp['screen_name'],
                token=resp['oauth_token'], secret=resp['oauth_token_secret'])
    login_user(user)
    user.user_id = session['user_id']
    users.append(user)
    mongo.db.participants.insert(user.save_participant())
    return redirect(request.args.get('next') or url_for('home', username=user.username))


@app.route('/google')
def google():
    return 'Google'


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'USAGE: python commpute.py <address> <port>'
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
