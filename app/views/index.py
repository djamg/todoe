from flask import render_template, request, Blueprint
from app import app, db, mail
from app.models.waitlist import Waitlist
from flask_login import current_user
from flask_mail import Message


@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method=="POST":
        email_id = request.form['email']
        new_signup = Waitlist(email_id = email_id)
        try:
            if bool(Waitlist.query.filter_by(email_id=email_id).first()):
                return render_template('create.html', text="You have already signed up! ",email_id=email_id)
                
            else:
                db.session.add(new_signup)
                db.session.commit()
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=email_id, current_user=current_user)
        except:
            "There was a problem signing up"

# @app.route('/test_mail/<to>/<body>')
# def test_mail(to, body):
#     msg = Message(body,
#                   sender="amoghdevelopment@gmail.com",
#                   recipients=[to])
#     mail.send(msg)
#     return "Mail sent"

