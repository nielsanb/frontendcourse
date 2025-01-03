from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from website.config.generic import SECRET_KEY, DB_NAME

#Instantiate a db-object outside the create_app function.
db = SQLAlchemy()

#app will be initialized in the main.py
def create_app():
    #1. initialize flask-app
    app = Flask(__name__)

    #2. import configs
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #3. Register the different files that contain routes (via blueprints)
    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #4. Import the database model objects
    from website.models import User, Note

    #5. Connect db and app
    db.init_app(app)

    #6. Create the models in the database, if not yet exist
    with app.app_context():
        if not path.exists('instance/' + DB_NAME):
            db.create_all()
            print('Created Database!')

    #7. Init Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #Where to redirect if no login?
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #.get -> primary key, .filter_by(field=value) -> whatever field you want
    
    return app