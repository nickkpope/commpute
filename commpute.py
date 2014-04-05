# all the imports
from flask import session, redirect, url_for, render_template, flash, request
from flask.ext.login import login_required, logout_user
from ops import app, facebook, twitter


@app.route('/')
def show_landing():
    return render_template('landing.html')


@app.route('/login')
def login():

    # form = LoginForm()
    # if form.validate_on_submit():
    #   #validate user here
    #   user = User('John')
    #   login_user(user)
    #   flash("Logged in successfully.")
    #   return redirect(url_for('profile', username='John'))

    return render_template("login.html")


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
def profile(username):
    return 'Welcome %s to your profile page!' % username


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


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
    else:
        session['twitter_oauth'] = resp
    return redirect(url_for('profile', username='Twitter'))


@app.route('/google')
def google():
    return 'Google'


if __name__ == '__main__':
    app.run()
