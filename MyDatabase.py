import pymongo
from abc import ABC, abstractmethod

class DatabaseBase(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def getDB(self):
        pass

class MyDatabase(DatabaseBase):
    def __init__(self):
        super().__init__()
        self.db_name = "DMML"#db_name
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        print("Successfully connected to MySQL database!")

    def getDB(self):
        db = self.connection[self.db_name]
        return db