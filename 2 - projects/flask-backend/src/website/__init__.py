from flask import Flask

from website.config.generic import SECRET_KEY


def create_app():
    #initialize
    app = Flask(__name__)

    #config
    app.config['SECRET_KEY'] = SECRET_KEY

    #register the different files that contain routes
    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app