from flask import Blueprint, render_template, request, flash,redirect,url_for
from string import digits
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User,File
from flask_login import login_user,login_required,logout_user,current_user

#from models import File
import os

#defining Blueprint for flask application

auth = Blueprint('auth',__name__)

##Methods specifies which kind of request can be handled
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        ##Querying database to see if user exits
        user = User.query.filter_by(email=email).first()
        if user:
            ## if user is found check password
            if check_password_hash(user.password,password):
                flash('You are now logged in', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exits', category='error')
    
    return render_template('login.html', user = current_user)

## Login_requered: Decorator that user needs to be logged in to be able to log out
@auth.route('/logout')
@login_required
def logout():
    ## Direct to login page
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwordOne = request.form.get('passwordOne')
        passwordTwo = request.form.get('passwordTwo')

        ## Checking that user does not already exits by the email

        user = User.query.filter_by(email=email).first()

        ## Checking that information is valid
        ## if is not valid alert user using flash

        if user:
            flash('Email already exits in database', category='error')
        elif len(email) < 3 or '@' not in email:
            flash("Email not valid too short or missing @", category='error')
        elif len(firstName) < 2 or digits in firstName:
            flash("Name not valid too short or has invalid characters", category='error')
        elif passwordOne != passwordTwo:
            flash("Passwords don't match", category='error')
        elif len(passwordOne) < 8:
            flash("Password too short must be at least 8 characters.", category='error')
        else:
            ## Defined user
            new_user = User(email = email, first_name= firstName, password=generate_password_hash(passwordOne, method='sha256'))
            ## add to database
            db.session.add(new_user)
            #update database/commit changes
            db.session.commit()
            login_user(user,remember=True)
            
            flash('Succesfully created account', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user = current_user)

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