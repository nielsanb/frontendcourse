from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    from webnotes.views import views
    from webnotes.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app