from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from website.models import User
from website import db


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #Catch the input
        signup_email = request.form.get('signup_email')
        signup_firstname = request.form.get('signup_firstname')
        signup_age = request.form.get('signup_age')
        signup_password = request.form.get('signup_password')
        signup_password_confirmation = request.form.get('signup_password_confirmation')

        #Validate the input
        if len(signup_email) < 6:
            flash('Email should be greater than 5 characters', category='error')
        elif len(signup_firstname) < 2:
            flash('Firstname should be greater than 1 character', category='error')
        elif len(signup_age) < 1:
            flash('Age invalid', category='error')
        elif len(signup_password) < 8:
            flash('Password must be at least 8 characters long', category='error')
        elif signup_password != signup_password_confirmation:
            flash('Passwords do not match! Please enter the passwords correctly the same.', category='error')
        elif User.query.filter_by(email=signup_email).first():
            flash('User already exists.', category='error')
        else:
        #create new user
            new_user = User(
                email = signup_email,
                firstname = signup_firstname,
                age = signup_age,
                #generate_password_hash: uses a (oneway) hash, extra salt to ensure that if two users have the same password, then still the hash is unique.
                password = generate_password_hash(signup_password, method='pbkdf2:sha256', salt_length=16)
            )
            
            #add to database
            db.session.add(new_user)
            db.session.commit()

            #login user
            login_user(new_user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('auth.signup_complete', current_user=current_user))
        
    return render_template('signup.html', current_user=current_user)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #Catch the input
        login_email = request.form.get('login_email')
        login_password = request.form.get('login_password')
        
        #Validate the input
        existing_user = User.query.filter_by(email=login_email).first()
        
        if existing_user:
            if check_password_hash(existing_user.password, login_password):
                #Login
                login_user(existing_user, remember=True)
                flash('Loggedin succesfully', category='success')
                return redirect(url_for('auth.login_complete', current_user=current_user))
            else:
                flash('Password incorrect', category='error')
                return render_template('login.html', current_user=current_user)
        else:
            flash('Something went wrong.', category='error')
            return render_template('login.html', current_user=current_user)

    elif request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for('auth.myaccount', current_user=current_user))
        else:
            return render_template('login.html', current_user=current_user)


@auth.route('/signup_complete')
@login_required
def signup_complete():
    return render_template('signup_complete.html', current_user=current_user)


@auth.route('/login_complete')
@login_required
def login_complete():
    return render_template('login_complete.html', current_user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You succesfully logged out!')
    return redirect(url_for('auth.login', current_user=current_user))


@auth.route('/myaccount')
@login_required
def myaccount():
    return render_template('myaccount.html', current_user=current_user)