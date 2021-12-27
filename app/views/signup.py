from os import chflags
from flask import render_template, request, redirect, flash
from app import app, db, mail
from app.models.profile import Profile
from app.models.user import User
from app.views import index 
from werkzeug.security import generate_password_hash, check_password_hash
import random
from app.views.profile import profile
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from flask import url_for
from flask_mail import Message
from flask_login import login_user

pic_list = ['a','b','c','d','e','f','g','h','i']


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email_id = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email_id=email_id).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index'))

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
                flash('You have already Signed up')
                return render_template('signup.html')
                
            else:
                db.session.add(newUser)
                token = generate_confirmation_token(newUser.email_id)
                db.session.commit()
                newProfile = Profile(profile_picture=random.choice(pic_list), user_id=newUser.id)
                print("--------------------------------------", newUser.id)
                db.session.add(newProfile)
                db.session.commit()
                confirm_url = url_for('confirm_email', token=token, _external=True)
                print("--------------------------------------", confirm_url)
                html = render_template('activate.html', confirm_url=confirm_url)
                subject = "Please confirm your email"
                send_email(newUser.email_id, subject, html)

                login_user(newUser)

                flash('A confirmation email has been sent via email.', 'success')
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=name)
        except:
            "There was a problem signing up"
        return render_template('index.html')

