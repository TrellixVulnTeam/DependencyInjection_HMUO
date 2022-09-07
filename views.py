from flask import render_template
from dependency_injector.wiring import inject, Provide
from .containers import MainContainer
#from MainService import DBService
from .services import DBService
#from Services.FacebookAdsTracker import facebook_ads_tracker_service
@inject
def index(db_service:DBService  = Provide[MainContainer.main_db]):
    #query = request.args.get("query", "Dependency Injector")
    #limit = request.args.get("limit", 10, int)
    db = db_service.get_connection()
    print("db connection:", db)
    return render_template(
        'index.html',
        value = "Main Page"
    )
def fbad_home():
    #query = request.args.get("query", "Dependency Injector")
    #limit = request.args.get("limit", 10, int)
    #repositories = []
    return render_template(
        'index.html',
        value = "FB Ad Tracker" 
    )
