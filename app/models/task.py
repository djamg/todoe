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

    def __repr__(self):
        return '<Task %s>'%self.id

    def get_remaining_time(self):
        return datetime.strptime(str(self.end_date),'%Y-%m-%d %H:%M:%S') - datetime.utcnow()

    def get_remaining_time_percentage(self):
        return datetime.strptime(str(self.end_date),'%Y-%m-%d %H:%M:%S') - datetime.utcnow()
