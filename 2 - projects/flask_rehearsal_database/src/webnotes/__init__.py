from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from webnotes.config import DB_NAME, SECRET_KEY

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from webnotes.views import views
    from webnotes.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    #Create the database
    from webnotes.models import User

    with app.app_context():
        if not path.exists('webnotes/' + DB_NAME):
            db.create_all()
            print('Created Database!')    

    return app