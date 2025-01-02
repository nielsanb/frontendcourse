from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from website.config.generic import SECRET_KEY, DB_NAME

db = SQLAlchemy()

#app will be initialized in the main.py
def create_app():
    #initialize app
    app = Flask(__name__)

    #config
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlte:///{DB_NAME}'

    db.init_app(app)

    #register the different files that contain routes
    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app