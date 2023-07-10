'''Application factory function
Some credits to Miguel Grinberg's flask tutorial:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://github.com/miguelgrinberg/microblog/
https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/
mostly the use of UserMixin and separation of concerns'''

import secrets
from flask import Flask
from flask_login import LoginManager

# needed for session/privacy control
login_manager = LoginManager()

def create_app():
    '''Creates instance of Flask application'''
    app = Flask(__name__)
    login_manager.init_app(app)
    # need a secret key for CSRF protection
    secret_key = secrets.token_hex()
    app.config["SECRET_KEY"] = secret_key
    return app
