from MyContainer import MyContainer
from flask import Flask
from flask_bootstrap import Bootstrap
import views

def create_app():
    container = MyContainer()
    # You can give configurations using yml file
    # container.config.from_yaml('config.yml')

    app = Flask(__name__)
    app.container = container
    app.add_url_rule('/', 'index', views.index)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    return app