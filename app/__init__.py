from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('../config.py')

# app.secret_key = "super secret key"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoe.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


from app.views import *


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)