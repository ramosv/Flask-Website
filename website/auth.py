from flask import Blueprint, render_template, request, flash,redirect,url_for
from string import digits
from werkzeug.utils import secure_filename
from . import db
#from models import File
import os

#defining Blueprint for flask application

auth = Blueprint('auth',__name__)

##Methods specifies which kind of request can be handled
@auth.route('/login', methods=['GET','POST'])
def login():
    #Store data from form as a ImmutableMultiDict [('email', 'vicnte@fskd.com'), ('password', 'sdfs')]
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwordOne = request.form.get('passwordOne')
        passwordTwo = request.form.get('passwordTwo')


        ## Checking that information is valid
        ## if is not valid alert user using flash
        if len(email) < 3 or '@' not in email:
            flash("Email not valid too short or missing @", category='error')
        elif len(firstName) < 2 or digits in firstName:
            flash("Name not valid too short or has invalid characters", category='error')
        elif passwordOne != passwordTwo:
            flash("Passwords don't match", category='error')
        elif len(passwordOne) < 8:
            flash("Password too short must be at least 8 characters.", category='error')
        else:
            ## Add to database
            flash('Succesfully created account', category='success')
            


    return render_template("sign_up.html")

@auth.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        new_filename = secure_filename(f.filename)
        f.save(os.path.join(auth.config['UPLOAD_FOLDER'], new_filename))  # You should define UPLOAD_FOLDER in your config
        #new_file = File(filename=new_filename, user_id=current_user.id)  # Assuming you're using Flask-Login for user management
        #db.session.add(new_file)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload.html')