from flask import render_template, request, Blueprint, 
from app import app, db
from app.models.profile import Profile 



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
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=email_id)
        except:
            "There was a problem signing up"

