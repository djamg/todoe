from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile
from app.models.user import User
from app.views import index 
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/signup',methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        name = request.form['name']
        email_id = request.form['email']
        user_name = request.form['username']
        password = request.form['password']
        newUser = User(name = name, email_id = email_id, user_name = user_name, password = generate_password_hash(password, method='sha256') )
        try:
            if bool(User.query.filter_by(email_id=email_id).first()):
                return render_template('create.html', text="You have already signed up! ",email_id=email_id)
                
            else:
                db.session.add(newUser)
                db.session.commit()
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=name)
        except:
            "There was a problem signing up"
        return render_template('index.html')