from flask import g, session
from ops import app, login_manager, facebook, twitter, users


@facebook.tokengetter
def get_facebook_token():
    if 'facebook_oauth' in session:
        resp = session['facebook_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@twitter.tokengetter
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
    for user in users:
        if user.userid == userid:
            return user


class User:

    def __init__(self, username, token, secret):
        self.username = username
        self.token = token
        self.secret = secret
        self.userid = None

    def is_authenticated(self):
        '''Determines whether a user has provided the correct crudentials'''
        return True

    def is_active(self):
        '''Determines whether a user is an active user i.e. not suspended'''
        return True

    def is_anonymous(self):
        '''Determines whether the user is anonymous
        (real users should return false)'''
        return False

    def get_id(self):
        '''Return the id of the user (the id must be in unicode)'''
        return u'5'

    def get(self):
        return self.username
