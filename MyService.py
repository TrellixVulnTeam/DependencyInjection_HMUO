from injector import inject
from MyDatabase import DatabaseBase
class MyService:
    @inject
    def __init__(self, connection: DatabaseBase):
        print(f"DatabaseBase instance is {connection}")
        self.connection = connection

    def get_data(self):
        database = self.connection.getDB()
        cursor = database["FB_ads_table"]
        data = cursor.find({})
        return data
