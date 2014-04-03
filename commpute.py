# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.login import LoginManager, login_required, login_user
from auth import *
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def show_landing():
    return render_template('landing.html')

@app.route('/login')
def login():
	'''
	form = LoginForm()
	if form.validate_on_submit():
		#validate user here
		user = User('John')
		login_user(user)
		flash("Logged in successfully.")
		return redirect(url_for('profile', username='John'))
	'''
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

#@login_required
@app.route('/profile/<username>')
def profile(username):
	return 'Welcome %s to your profile page!' % username

@login_required
@app.route('/logout')
def logout():
	logout_user()
	return redirect('/')

@app.route('/facebook')
def facebook():
	return 'Facebook'

@app.route('/twitter')
def twitter():
	callback_url = url_for('twitter-auth', username='Twitter')
	return twitter.authorize(callback=callback_url)

@app.route('/twitter-auth')
@twitter.authorized_handler
def twitter_auth(resp):
	if resp is None:
		flash('You denied the request to sign in.')
	else:
		session['twitter_oauth'] = resp
	return redirect(url_for('profile'))

@app.route('/google')
def google():
	return 'Google'


if __name__ == '__main__':
    app.run()
