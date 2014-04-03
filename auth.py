from flask import g, session
from flask.ext.login import LoginManager, login_user, logout_user
from flask.ext.login import current_user, login_required
from commpute import app, login_manager
from flask_oauthlib.client import OAuth

#Oauth Setup
oauth = OAuth(app)

twitter = oauth.remote_app('twitter',
	base_url = 'https://api.twitter.com/1/',
	request_token_url='https://api.twitter.com/oauth/request_token',
	access_token_url='https://api.twitter.com/oauth/access_token',
	authorize_url='https://api.twitter.com/oauth/authenticate',
	consumer_key='',
	consumer_secret=''
)

@twitter_tokengetter
def get_twitter_token():
	if 'twitter_oauth' in session:
		resp = session['twitter_oauth']
		return resp['oauth_token'], resp['oauth_token_secret']

@app.before_request
def before_request():
	g.user = None
	if 'twitter_oauth' in session:
		g.user = session['twitter_oauth']

#Login Customization
login_manager.login_view = 'login'
login_manager.login_message = u'Please log in to access this page'

@login_manager.user_loader
def load_user(userid):
	return User('John')

class User:

	def __init__(self, name):
		self.name = name
		self.authenticated = True		

#Determines whether a user has provided the correct crudentials
	def	is_authenticated(self):
		return self.authenticated

#Determines whether a user is an active user i.e. not suspended
	def is_active(self):
		return True
		
#Determines whether the user is anonymous (real users should return false)
	def is_anonymous(self):
		return false

#Return the id of the user (the id must be in unicode)
	def get_id(self):
		return u'5'
