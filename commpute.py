# all the imports
from flask import session, redirect, url_for, render_template, flash, request, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user
from ops import app, facebook, twitter, mongo, users
from auth import User
import time
import pymongo


@app.route('/')
def show_landing():
    return render_template('landing.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('profile', username=current_user.username))
    if request.method == 'POST':
        stored_user = mongo.db.users.find_one({'username': request.form['username']})
        if stored_user is not None:
            user = User(username=stored_user['username'], name=stored_user['name'])
            login_user(user)
            users.append(user)
            user.user_id = session['user_id']
            return redirect(url_for('profile', username=user.username))
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_landing'))


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/add')
def index():
    return render_template('jstest.html')


@app.route('/progress')
def progress():
    return jsonify(prog=time.time() % 50 * 2, jobs=jobs)


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated():
        return redirect(url_for('profile', username=current_user.username))
    if request.method == 'POST':
        user = User(request.form['username'], request.form['name'])
        users.append(user)
        login_user(user)
        user.user_id = session['user_id']
        mongo.db.users.insert(user.save_participant())
        return redirect(url_for('profile', username=user.username))
    return render_template('signup.html')


@app.route('/docs')
def docs():
    return 'Docs'


@app.route('/testdrive')
def test_drive():
    return render_template('jobs.html', jobs=jobs)


@app.route('/profile/<username>')
@login_required
def profile(username):
    for user in users:
        if user.username == username:
            return render_template('home.html', name=user.name)
    return render_template('home.html')


jobs = [
    {
        'name': 'Job 1',
        "id": 'j1',
        'tasks': [
            {'name': 'Task 1', 'id': 't1'},
            {'name': 'Task 2', 'id': 't2'}
        ]
    },
    {
        'name': 'Job 2',
        "id": 'j2',
        'tasks': [
            {'name': 'Task A', 'id': 't1'},
            {'name': 'Task B', 'id': 't2'},
            {'name': 'Task C', 'id': 't3'}
        ]
    },
    {
        'name': 'Job 3',
        "id": 'j3',
        'tasks': [
            {'name': 'Task Gorilla', 'id': 't1'},
            {'name': 'Task Banana', 'id': 't2'},
            {'name': 'Task Drunk', 'id': 't3'},
            {'name': 'Task Monkey', 'id': 't4'}

        ]
    }
]


@app.route('/facebook')
def facebook_login():
    callback_url = url_for('facebook_auth')
    return facebook.authorize(callback=callback_url, next=request.args.get('next'))


@app.route('/facebook_auth')
@facebook.authorized_handler
def facebook_auth(resp):
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['facebook_oauth'] = resp
    return redirect(url_for('profile', username='Facebook'))


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
    user = None
    for i in users:
        if i.username == resp['screen_name']:
            user = i

    if user is None:
        user = User(resp['screen_name'], resp['oauth_token'], resp['oauth_token_secret'])
        print session
        user.userid = session['user_id']
        users.append(user)
        login_user(user)
    else:
        login_user(user)

    return redirect(request.args.get('next') or url_for('profile', username=user.username))


@app.route('/google')
def google():
    return 'Google'


if __name__ == '__main__':
    app.run(host='107.170.57.29', port=80)
