from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Organization %s>'%self.id

