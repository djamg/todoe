from flask import render_template, request, redirect
from app import app, db
from app.models.profile import Profile 

# about page2
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')