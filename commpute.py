# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.login import LoginManager
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
	return 'Login'

@app.route('/signup')
def sign_up():
	return 'Sign Up'

@app.route('/docs')
def docs():
	return 'Docs'

@app.route('/testdrive')
def test_drive():
	return 'Test Drive'


if __name__ == '__main__':
    app.run()
