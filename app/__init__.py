from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__)
app.secret_key = "super secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.views import *


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)