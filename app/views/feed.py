from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile 


@app.route('/feed', methods=['GET'])
def feed():
    return render_template('feed.html')