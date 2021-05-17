from dependency_injector import containers, providers
from MyService import MyService

class MyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()
    db_connection = providers.Factory(
        MyService.get_connection,
        token="token HERE"
    )

    print_service = providers.Factory(
        MyService.print_tables,
        db_connection = db_connection
    )
