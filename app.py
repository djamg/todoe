from enum import unique
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserSignUp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email_id = db.Column(db.String(100), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Name %>'%self.id

@app.route('/',methods=["GET"])
def hello_world():
    return render_template('home.html')


@app.route('/sign_in',methods=["GET"])
def sign_in():
    return render_template('sign_in.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/create',methods=["GET", "POST"])
def create():
    if request.method == "POST":
        email_id = request.form['email']
        new_signup = UserSignUp(email_id = email_id)
        try:
            if bool(UserSignUp.query.filter_by(email_id=email_id).first()):
                return render_template('create.html', text="You have already signed up! ")
                
            else:
                db.session.add(new_signup)
                db.session.commit()
                return render_template('create.html', textAlready="Thanks for signing up! " ,email_id=email_id)
        except:
            "There was a problem signing up"

    else:
        return "ERROR | Route not found"
    
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)