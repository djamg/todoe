from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile
from flask_login import login_required


@app.route('/feed', methods=['GET'])
@login_required
def feed():
    return render_template('feed.html')