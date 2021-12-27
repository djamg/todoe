from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    user_name = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    tasks = db.relationship('Task', backref='user')
    comments = db.relationship('Comment', backref='user')
    profile = db.relationship('Profile', backref='user')
    confirmed = db.Column(db.Integer)
    confirmed_on = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<User%s>'%self.id

    