from sqlalchemy.orm import backref
from app import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    complete = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    comments = db.relationship("Comment", backref="task")

    def __repr__(self):
        return '<Task %s>'%self.id

    def get_remaining_days(self):
        days_remaining = (self.end_date-datetime.utcnow())
        return days_remaining

    def get_remaining_days_percentage(self):
        days_remaining_percentage = 100-(self.end_date-datetime.utcnow())/(self.end_date-self.date_created)*100
        return days_remaining_percentage
