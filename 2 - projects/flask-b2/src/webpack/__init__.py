from flask import Flask

def create_app():
    app = Flask(__name__)

    from webpack.views import views
    from webpack.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app