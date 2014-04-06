from flask import Flask
from flask.ext.login import LoginManager
import os
from flask_oauthlib.client import OAuth


#Create and configure the application
app = Flask(__name__)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

#Oauth Setup
oauth = OAuth(app)

#Facebook
facebook = oauth.remote_app('facebook',
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='188477911223606',
    consumer_secret='621413ddea2bcc5b2e83d42fc40495de',
)


#Twitter
twitter = oauth.remote_app('twitter',
    base_url = 'https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    #consumer_key='FW0k326IPRWRB6cPd6AEw',
    #consumer_secret='OVLhEfVm5ZaU8XHPWaFosenmDm4o3uj0fDi3E0KfQ'
    #Using the keys for flask oauth example
    consumer_key='xBeXxg9lyElUgwZT6AZ0A',
    consumer_secret='aawnSpNTOVuDCjx7HMh6uSXetjNN8zWLpZwCEU4LBrk'
)


