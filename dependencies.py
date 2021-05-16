from injector import singleton
from MyDatabase import DatabaseBase, MyDatabase
from facebook_ads_tracker_service import facebook_ads_tracker_service
from MyService import MyService
def configure(binder):
    binder.bind(facebook_ads_tracker_service, to=facebook_ads_tracker_service, scope=singleton)
    binder.bind(DatabaseBase, to=MyDatabase, scope=singleton)
