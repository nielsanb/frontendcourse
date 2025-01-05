from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path

#Maak db object van 
db = SQLAlchemy()

def create_app():
    #Maak app object
    app = Flask(__name__)

    #Config
    app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI']

    db.init_app(app)

    #
    from webpack.views import views
    from webpack.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from webpack.models import User, Note

    with app.app_context():
        if not path.exists('webpack/' + DB_NAME):
            db_create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id)
        return User.query.get(int(id))
    
    return app






    #app (init)
    #config
    #database (init + connect)
    #blueprints
    #models
    #login_manager (init + connect)