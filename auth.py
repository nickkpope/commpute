from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import LoginManager, login_user, logout_user
from flask.ext.login import current_user, login_required
from commpute import app, login_manager

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
