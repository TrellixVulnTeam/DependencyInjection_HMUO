from flask import render_template
from dependency_injector.wiring import inject, Provide
from MyContainer import MyContainer
from MyService import MyService

@inject
def index(service: MyService = Provide[MyContainer.print_service]):
    db_connection = service.get_connection()
    table_names = service.print_tables(db_connection)

    return render_template(
        'index.html',
        db_connection=db_connection,
        table_names=table_names
    )