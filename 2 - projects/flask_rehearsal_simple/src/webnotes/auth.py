from flask import Blueprint, render_template, request, make_response

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