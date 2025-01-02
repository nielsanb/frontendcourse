from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

from website.config.generic import SECRET_KEY, DB_NAME

db = SQLAlchemy()

#app will be initialized in the main.py
def create_app():
    #initialize flask-app
    app = Flask(__name__)

    #config
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #register the different files that contain routes
    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #We import the models module, just to make just the script runs 
    #, and therewith defines the models, before the database is initialized.
    from website.models import User, Note

    #Connect db and app
    db.init_app(app)

    with app.app_context():
        if not path.exists('instance/' + DB_NAME):
            db.create_all()
            print('Created Database!')
    
    return app