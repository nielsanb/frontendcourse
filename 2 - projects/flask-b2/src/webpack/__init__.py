from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

from os import path

from webpack.config.config import SECRET_KEY, DB_NAME

db = SQLAlchemy()

def create_app():
    #Inititialize the app
    app = Flask(__name__)

    #Get secret for forms, sessions and cookies
    app.config['SECRET_KEY'] = SECRET_KEY

    #Setup database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #Import and register blueprints
    from webpack.views import views
    from webpack.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    #Create database
    from webpack.models import User, Note

    with app.app_context():
        if not path.exists('webpack/' + DB_NAME):
            db.create_all()
            print('Created Database!')

    #Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #view to redirect to if no login.
    login_manager.init_app(app)

    #Telling flask how to load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #get looks directly at the primary key

    return app