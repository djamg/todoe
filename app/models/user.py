from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email_id = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    user_name = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return '<User%>'%self.id
