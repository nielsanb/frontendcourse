from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #Input validation
        email = request.form.get('login_email')
        password = request.form.get('login_password')
        return render_template('login_complete.html', email=email)    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #Catch the input
        email = request.form.get('signup_email')
        firstname = request.form.get('signup_firstname')
        age = request.form.get('signup_age')
        signuppassword = request.form.get('signup_password')
        confirmationpassword = request.form.get('signup_password_confirmation')

        #Validate the input
        if len(email) < 6:
            flash('Email should be greater than 5 characters', category='error')
        elif len(firstname) < 2:
            flash('Firstname should be greater than 1 character', category='error')
        elif len(age) < 1:
            flash('Age invalid', category='error')
        elif len(signuppassword) < 8:
            flash('Password must be at least 8 characters long', category='error')
        elif signuppassword != confirmationpassword:
            flash('Passwords do not match! Please enter the passwords correctly the same.', category='error')
        else:
            flash('Account created!', category='success')
            return render_template('signup_complete.html', firstname=firstname, email=email)
        
    return render_template('signup.html')