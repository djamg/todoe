from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile
from app.models.organization import Organization


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')