from app import db
from datetime import datetime


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    profile_picture = db.Column(db.String(100), default = "a")
    website = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    bio = db.Column(db.String(200))
    city = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Profile %s>'%self.id
