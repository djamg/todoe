from app import db
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)

    def __repr__(self):
        return '<Comment %s>'%self.id
