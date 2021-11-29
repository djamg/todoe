import re
from flask import render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from app.models.profile import Profile 
from app.models.user import User 


@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
         # login code goes here
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        user = User.query.filter_by(email_id=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template('login.html') # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        print("Checks passed")
        return render_template('create.html', textAlready="Successfully LOGGED IN", email_id="checks passed")