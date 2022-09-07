from .containers import MainContainer
from flask import Flask
from flask_bootstrap import Bootstrap
from . import views

def create_app():
    container = MainContainer()

    app = Flask(__name__)
    app.container = container

    "Main Page"
    app.add_url_rule('/', 'index', views.index)

    "FBADTracker"
    app.add_url_rule('/facebook_ads_tracker', 'fbad_home', views.fbad_home)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    return app
