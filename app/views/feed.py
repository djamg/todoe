from flask import render_template, request, redirect
from flask.helpers import url_for
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.functions import user
from app import app, db
from flask_login import login_required
from app.models.task import Task
from app.models.user import User

from datetime import datetime
from flask_login import current_user
from sqlalchemy import select


@app.route('/feed', methods=['GET'])
@login_required
def feed():
    cards = db.session.query(Task).filter_by(complete = 0).order_by(Task.end_date).all()
    # print('-----------------------------------------')
    # print(cards[3].get_remaining_days())
    # print(cards[3].get_remaining_days_percentage())
    completed_cards = db.session.query(Task).filter_by(complete = 1).order_by(Task.end_date).all()
    return render_template('feed.html', cards=cards, completed_cards=completed_cards)

@app.route('/time/<id>')
def time(id):
    task = Task.query.filter_by(id=int(id)).first()
    return str(task.get_remaining_time_percentage())

@app.route('/fetch_all_cards')
@login_required
def fetch_all_cards():
    cards = db.session.query(Task).filter_by(user_id=current_user.id).order_by(Task.end_date).all()
    return render_template('feed.html', cards=cards, current_user=current_user)


@app.route('/complete/<id>')
@login_required
def complete(id):
    task = Task.query.filter_by(id=int(id)).first()
    if current_user.id == task.user_id:
        task.complete = not task.complete
        db.session.commit()
    return redirect(url_for('feed'))

@app.route('/delete/<id>')
@login_required
def delete_card(id):
    card_to_delete = Task.query.filter_by(id=int(id)).first()
    if current_user.id == card_to_delete.user_id:
        db.session.delete(card_to_delete)
        db.session.commit()
    return redirect(url_for('feed'))