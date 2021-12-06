from flask import render_template, request, Blueprint
from app import app, db
from app.models.profile import Profile 
from flask_login import current_user


@app.route('/',methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method=="POST":
        email_id = request.form['email']
        new_signup = Profile(email_id = email_id)
        try:
            if bool(Profile.query.filter_by(email_id=email_id).first()):
                return render_template('create.html', text="You have already signed up! ",email_id=email_id)
                
            else:
                db.session.add(new_signup)
                db.session.commit()
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=email_id, current_user=current_user)
        except:
            "There was a problem signing up"

@app.route('/list')
def listTasks():
    pass
