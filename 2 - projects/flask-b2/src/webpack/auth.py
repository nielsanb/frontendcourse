from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from webpack.models import User
from webpack import db 

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #Catch variables
        signup_firstname = request.form.get('signup_firstname')
        signup_age = request.form.get('signup_age')
        signup_email = request.form.get('signup_email')
        signup_password = request.form.get('signup_password')
        signup_password_confirmation = request.form.get('signup_password_confirmation')
        print(signup_firstname, signup_age, signup_email, signup_password, signup_password_confirmation)

        #Validation
            #validate each field
            #validate if emailadres does not yet exists

        #Create new user
        new_user = User(
            email = signup_email,
            password = generate_password_hash(signup_password, method='pbkdf2:sha256'),
            firstname = signup_firstname,
            age = signup_age
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.account', user=current_user))


    return render_template('signup.html', user=current_user)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_email = request.form.get('login_email')
        login_password = request.form.get('login_password')
        
        #Validation
        user = User.query.filter_by(email=login_email).first()
        if user:
            if check_password_hash(user.password, login_password):
                pass #user exists, password correct
                login_user(user, remember=True)
                return redirect(url_for('auth.account', user=current_user))
            else:
                pass #user exists, password wrong
        
        else:
            pass #email does not exist

        print(login_email, login_password)

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login', user=current_user))


@auth.route('/account')
@login_required
def account():
    return render_template('account.html', user=current_user)