from flask import Flask, request, render_template, redirect, url_for
from flask_injector import FlaskInjector
from injector import inject
from MyService import MyService
from facebook_ads_tracker_service import facebook_ads_tracker_service

from dependencies import configure

app = Flask(__name__)

@inject
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tweet_tracker')
def tweet_tracker(service: MyService):
    print(f"MyService instance is {service}")
    return render_template("tweet_tracker.html")

@app.route('/facebook_ads_tracker')
def facebook_ads_tracker(service: facebook_ads_tracker_service):
    print(f"MyService instance is {service}")
    return render_template("facebook_ads_tracker.html")


@app.route('/facebook_ads_tracker/get_db')
def get_facebook_ads_client(service: facebook_ads_tracker_service):
    print(f"MyService instance is {service}")
    return render_template("facebook_ads_tracker.html", data=service.get_data())

@app.route('/facebook_ads_tracker/set_db')
def set_facebook_ads_client(service: facebook_ads_tracker_service):
    print(f"MyService instance is {service}")
    return render_template("facebook_ads_tracker.html", data=service.set_data(instance = "donald trump"))

if __name__ == "__main__":
    FlaskInjector(app=app, modules=[configure])
    app.run(host='0.0.0.0', port=5000, debug=True)
