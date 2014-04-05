# all the imports
from flask import session, redirect, url_for, render_template, flash, request
from flask.ext.login import login_required, login_user, logout_user, current_user
from ops import app, facebook, twitter, users
from auth import User


@app.route('/')
def show_landing():
    return render_template('landing.html')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    current_user.authenticated = False
    logout_user()
    return redirect(url_for('show_landing'))


@app.route('/signup')
def sign_up():
    return 'Sign Up'


@app.route('/docs')
def docs():
    return 'Docs'


@app.route('/testdrive')
def test_drive():
    return 'Test Drive'


@app.route('/profile/<username>')
@login_required
def profile(username):
    return 'Welcome %s to your profile page!' % username


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
    app.run()
