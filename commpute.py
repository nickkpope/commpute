# all the imports
import sys
import socket
import errno
from flask import session, redirect, url_for, render_template, flash, request, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user
from ops import app, facebook, twitter, mongo
from auth import User
import time
from mock_data import jobs_data, updates
import db
import xmlrpclib
running_jobs = []
dist_proxy = xmlrpclib.ServerProxy('http://localhost:8090')


@app.route('/')
def show_landing():
    return render_template('landing.html', showbg=True)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('home', username=current_user.username))
    if request.method == 'POST':
        stored_user = db.find_user(request.form['username'])
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


@app.route('/progress', methods=['POST'])
@login_required
def progress():
    progress_report = []
    for job_id in running_jobs:
        progress_report.append({'jid': job_id, 'progress': getJobProgress(job_id)})
    return jsonify(jobs_progress=progress_report)


def getJobProgress(job_id):
    task_statuses = dist_proxy.system.getTaskStatuses(job_id)
    ret = {
        'active': task_statuses.count('EXECUTING'),
        'finished': task_statuses.count('COMPLETE'),
        'error': task_statuses.count('FAILED'),
        'total': dist_proxy.system.getTotalTasks(job_id)
    }
    print ret
    return ret
    # elif job_id == 'j2':
    #     return {'active': 7, 'finished': 13, 'error': 5, 'total': 40}
    # elif job_id == 'j3':
    #     return {'active': 1, 'finished': 20, 'error': 0, 'total': 21}


@app.route('/submit_job', methods=['POST'])
def submit_job():
    try:
        job_id = dist_proxy.system.submitRandomizedTestJob("oats", 10, 10)
        running_jobs.append(job_id)
        return jsonify(job_id=job_id)
    except socket.error:
        etype, evalue, etrace = sys.exc_info()
        if evalue.errno == errno.ECONNREFUSED:
            error = 'The Job driver XMLRPC server must not be running.'
        else:
            error = str(evalue)
        return jsonify(job_id=None, error=error)


@app.route('/kill_job', methods=['POST'])
def kill_job():
    job_id = request.form['job_id']
    try:
        running_jobs.remove(job_id)
        dist_proxy.system.cancelJob(job_id)
        return jsonify(nailedit=True)
    except:
        etype, evalue, etrace = sys.exc_info()
        print 'caught unhandled exception: %s' % evalue
        return jsonify(nailedit=False, error=evalue)


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
    query = request.form.get('query') or {}
    username = request.form.get('username') or query.get('username') or current_user.username
    item_data = find_items_by_type(item_type, q=query)
    print 'fetching items for', item_type, item_data
    return jsonify(item_data=item_data,
                   username=username,
                   html=render_template('items.html', item_type=item_type, items=item_data))


def find_items_by_type(item_type, q=None):
    item_map = {}
    item_map['friends'] = lambda q: contributors(current_user.username, q or {})
    item_map['friend_suggestions'] = lambda q: suggest_friends(current_user.username, q or {})
    item_map['jobs'] = get_active_jobs
    item_map['user_updates'] = lambda q: updates['user_updates']
    item_map['user_updates'] = lambda q: updates['user_updates']
    item_map['user_action_items'] = lambda q: updates['user_action_items']
    item_map['community_updates'] = lambda q: updates['community_updates']
    try:
        return list(item_map[item_type](q))
    except KeyError:
        print 'recieved bad item_type', item_type
        return []


def contributors(username, q=None):
    ret = []
    for f in db.find_user(username, q)['contributors']:
        f_doc = db.find_user(f, strip_id=True)
        if f_doc:
            ret.append(f_doc)
        else:
            print 'could not find', f
    return ret


def get_active_jobs(q={}):
    ret = []
    for job_id in running_jobs:
        ret.append({'id': job_id, 'name': job_id})
    return ret


@app.route('/iteminfo', methods=['POST'])
def item_info():
    item_id = request.form['item_id']
    item_type = request.form['item_type']
    for item in items[item_type]:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify(None)


@app.route('/fetch_user_computers/<username>')
def fetch_user_computers(username):
    print '>>', username
    user = db.find_user(username)
    print user['computers']
    if user:
        return jsonify(html=render_template('items.html', items=user['computers'], item_type='computers'),
                       item_data=user['computers'])
    else:
        return jsonify(html='No items found.',
                       item_data=[])


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

    return render_template('items.html', items=items[item_type], pane_id=pane_id, item_type=item_type)


@app.route('/jobs/<username>')
@login_required
def jobs(username):
    return render_template('jobs.html', username=username)


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
    print 'friends(%s)' % username
    return render_template('friends.html', username=username)


@app.route('/add_friend', methods=['POST'])
@login_required
def add_friend():
    return manage_friend(request.form['friend_username'], add=True)


@app.route('/remove_friend', methods=['POST'])
@login_required
def remove_friend():
    return manage_friend(request.form['friend_username'], remove=True)


def manage_friend(friend_username, add=False, remove=False):
    print 'add_friend(%s)' % friend_username
    user = db.Participant(current_user.username, load=True)
    if db.find_user(friend_username):
        try:
            if add:
                user['contributors'].append(friend_username)
            elif remove:
                user['contributors'].pop(user['contributors'].index(friend_username))
            user.save()
        except:
            print 'unknown error occured when managing friend'
            return jsonify(nailedit=False)
        return jsonify(nailedit=True)
    else:
        return jsonify(nailedit=False)


@app.route('/request_friend', methods=['POST'])
@login_required
def request_friend():
    friend_username = request.form['friend_username']
    db.FriendRequest(current_user.username, friend_username).insert()


def suggest_friends(username, q={}):
    '''returns 2nd degree connections as suggestions or
    all participants if no friends are found'''
    user = db.find_user(username)
    if not user:
        print 'could not find user', username
        return []
    ret = []
    if len(user['contributors']) == 0:
        return list(db.find_participants({'username': {'$ne': username}}))
    for cname in user['contributors']:
        c = db.find_user(cname)
        if c:
            for suggestion in [db.find_user(i, strip_id=True) for i in c['contributors']]:
                if suggestion and not suggestion['username'] in user['contributors']:
                    ret.append(suggestion)
    return ret


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
