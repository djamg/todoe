from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile
from app.models.task import Task
from app.models.user import User
from app.models.organization import Organization
from flask_login import current_user


@app.route('/profile', methods=['GET'])
def user_profile():
    cards = db.session.query(Task).filter_by(user_id=current_user.id).order_by(Task.end_date).all()
    completed_cards = db.session.query(Task).filter_by(user_id=current_user.id, complete = 1).order_by(Task.end_date).all()
    return render_template('profile.html', current_user=current_user, completed_cards=completed_cards, cards=cards)

@app.route('/profile/<user_name>', methods=['GET'])
def profile(user_name):
    user_id = User.query.filter_by(user_name=user_name).first().id
    cards = db.session.query(Task).filter_by(user_id=user_id, complete=0).order_by(Task.end_date).all()
    completed_cards = db.session.query(Task).filter_by(user_id=user_id, complete = 1).order_by(Task.end_date).all()
    return render_template('profile.html', current_user=current_user, completed_cards=completed_cards, cards=cards)