from flask import render_template, request, redirect
from app import app, db
from flask_login import login_required
from app.models.task import Task
from datetime import datetime



@app.route('/feed', methods=['GET'])
@login_required
def feed():
    return render_template('feed.html')

@app.route('/time/<id>')
def time(id):
    task = Task.query.filter_by(id=int(id)).first()
    return str(task.get_remaining_time_percentage())