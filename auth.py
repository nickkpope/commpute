from flask import g, session
from ops import app, login_manager, facebook, twitter, mongo, users
from flask.ext.login import current_user
from db import Participant
from ops import mongo


@facebook.tokengetter
def get_facebook_token():
    if 'facebook_oauth' in session:
        resp = session['facebook_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@twitter.tokengetter
def get_twitter_token():
    if current_user.is_authenticated():
        return (current_user.token, current_user.secret)
    else:
        return None


@login_manager.user_loader
def load_user(userid):
    serial_user = mongo.db.participants.find_one({'userid': userid})
    if serial_user is not None:
        user = User(serial_user['username'], serial_user['name'])
        user.load_participant(serial_user)
        return user


class User(Participant):

    def __init__(self, username=None, name=None, token=None, secret=None):
        Participant.__init__(self, username, name)
        self.user_id = 0
        self.token = token
        self.secret = secret

    def save_user(self):
        self.__dict__

    def load_user(self, data):
        pass

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

