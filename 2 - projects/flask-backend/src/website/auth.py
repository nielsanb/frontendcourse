from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #Input validation

        return render_template('signup.html')


    
    return render_template('signup.html')