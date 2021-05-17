from injector import inject
from MyDatabase import DatabaseBase
class MyService:
    @inject
    def __init__(self, connection: DatabaseBase):
        print(f"DatabaseBase instance is {connection}")
        self.connection = connection
        self.table_name = "TABLENAME"

    def get_connection(self):
        # database = self.connection.getDB()
        # cursor = database[self.table_name]
        # data = cursor.find({})
        print("db_connection success")

        return self.connection

    def print_tables(self, db_connection):
        print("db_connection object is 000", db_connection)
        return self.table_name