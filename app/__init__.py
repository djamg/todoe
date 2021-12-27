from enum import unique
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager
from flask_migrate import Migrate, migrate
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    }
)

app = Flask(__name__)
mail = Mail(app)
app.config.from_pyfile('../config.py')

# app.secret_key = "super secret key"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoe.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app,metadata=metadata)
migrate = Migrate()

login_manager = LoginManager()
login_manager.init_app(app)


from app.views import *
migrate.init_app(app,db,render_as_batch=True)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)