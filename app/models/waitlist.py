from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin



class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    approved = db.Column(db.Integer)

    def __repr__(self):
        return '<Waitlist%s>'%self.id