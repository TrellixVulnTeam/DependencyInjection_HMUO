#THIS APP IS THE MAIN PART OF DEPENDENCY INJECTION FOR OTHER MODULES
from .application import create_app
app = create_app()

#BELOW IS UJUN's EXPERIMENTATION(Another Way of Dependency Injection)
from injector import inject
from flask_injector import FlaskInjector
from flask import render_template
from dependencies import configure
from FacebookAdsTracker.facebook_ads_tracker_service import facebook_ads_tracker_service

@inject
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
    app.run(port=5000, debug=True)