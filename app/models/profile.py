from app import db
from datetime import datetime


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email_id = db.Column(db.String(100), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<UserSignUp %>'%self.id
