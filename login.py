from flask import render_template, redirect, url_for, request, flash
from flask_oauth import Oauth
from flask.ext.login import LoginManager, login_user, logout_user
from flask.ext.login import current_user, loging_required


login_manager = LoginManger()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'Please log in to access this page'

@login_manager.user_loader
def load_user(userid):
	return User()

class User():

#Determines whether a user has provided the correct crudentials
	def	is_authenticated(self):
		return True

#Determines whether a user is an active user i.e. not suspended
	def is_active()
		return True
		
#Determines whether the user is anonymous (real users should return false)
	def is_anonymous()
		return false

#Return the id of the user (the id must be in unicode)
	def get_id()
		return u'5'
