from dependency_injector import containers, providers
#from MainService import DBService
from . import services
#from Services.FacebookAdsTracker import facebook_ads_tracker_service as FBAD
import pymongo
class MainContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".views"])
    config = providers.Configuration()
    #config = providers.Configuration(yaml_files=["config.yml"])
    #db_connection = pymongo.MongoClient("mongodb://localhost:27017/")
    db_connection = "Some object"
    #MAIN PAGE#
    main_db = providers.Factory(
        services.DBService,
        db_connection=db_connection,
    )
    
    ##FBAD##
    #fbad_db_query = providers.Factory(
    #    FBAD.query_construct
    #)

