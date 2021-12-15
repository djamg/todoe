from flask import render_template, request, redirect, flash
from flask.helpers import url_for
from app import app, db
from app.models.profile import Profile
from app.models.user import User
from app.models.task import Task
from app.views import index 
from flask_login import current_user, login_required
from datetime import datetime

@app.route('/create_task',methods=["POST"])
@login_required
def create_task():
    title = request.form['task-title']
    description = request.form['task-description']
    end_date = request.form['task-end-date']
    organization_id = request.form['organization-id']
    print(title,description,end_date,organization_id)
    datetime_object = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
    print(datetime_object)
    newTask = Task(title=title, description=description,end_date=datetime_object,user_id=current_user.id,date_created=datetime.utcnow())
    db.session.add(newTask)
    db.session.commit()
    return redirect(url_for('feed'))
