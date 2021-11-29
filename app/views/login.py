from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile 

@app.route('/login',methods=["GET", "POST"])
def login():
    return render_template('login.html')