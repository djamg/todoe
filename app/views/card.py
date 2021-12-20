from flask import render_template, request, redirect
from flask.helpers import url_for
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.functions import user
from app import app, db
from flask_login import login_required
from app.models.task import Task
from app.models.user import User
from app.models.comment import Comment 

from datetime import datetime
from flask_login import current_user
from sqlalchemy import select

@app.route('/card/<id>', methods=['GET'])
@login_required
def card_page(id):
    single_card = Task.query.filter_by(id=int(id)).first()
    comments = db.session.query(Comment).filter_by(task_id=id).all()
    return render_template('card.html', single_card=single_card, comments=comments)