from flask import render_template, request, redirect
from app import app, db
from flask_login import login_required
from app.models.task import Task
from datetime import datetime
from flask_login import current_user


@app.route('/feed', methods=['GET'])
@login_required
def feed():
    cards = db.session.query(Task).filter_by(user_id=current_user.id).order_by(Task.end_date).all()
    return render_template('feed.html', cards=cards)

@app.route('/time/<id>')
def time(id):
    task = Task.query.filter_by(id=int(id)).first()
    return str(task.get_remaining_time_percentage())

@app.route('/fetch_all_cards')
@login_required
def fetch_all_cards():
    cards = db.session.query(Task).filter_by(user_id=current_user.id).order_by(Task.end_date).all()
    return render_template('feed.html', cards=cards)