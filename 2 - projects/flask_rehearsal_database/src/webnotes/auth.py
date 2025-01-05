from flask import Blueprint, render_template, request, make_response, redirect, url_for
from webnotes.models import User

from webnotes import db

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.data, request.form, request.method, request.cookies, request.accept_languages)

        email = request.form.get('login_email')
        password = request.form.get('login_password')
        cookie = request.cookies.get('userid')

        return render_template('account.html', email=email, password=password, cookie=cookie)
    else:
        response = make_response(render_template('login.html'))
        response.set_cookie(key="userid", value="aaaaaa-111111-bbbb")

        return response


@auth.route("/account")
def account():
    return render_template('account.html')


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register_firstname = request.form.get('register_firstname')
        register_age = request.form.get('register_age')
        register_email = request.form.get('register_email')
        register_password = request.form.get('register_password')

        #validatie: email al in de database?
        db_user = User.query.filter_by(email=register_email).first()

        if db_user:
            message = "User already exists"
            return render_template('register.html', message=message)
        
        else:
            #make the model object
            user = User(
                email = register_email,
                password = register_password,
                firstname = register_firstname,
                age = register_age
            )

        #send to db, via a session
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.account'))


    else:
        return render_template('register.html')