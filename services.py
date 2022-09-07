from injector import inject
from .MyDatabase import DatabaseBase

class DBService:
    #def __init__(self, db_connection: DatabaseBase):
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.table_name = "TABLENAME"

    def get_connection(self):
        print("db_object:")
        return self.db_connection

    def get_table(self, db_connection):
        print("db_connection object is 000", db_connection)
        # database = self.connection.getDB()
        # cursor = database[self.table_name]
        # data = cursor.find({})
        return self.table_name
