
class DBConnectionError(Exception):

    URL = "mongodb://atlas-sql-697a5032a5837bd058f9c46e-idzdis.a.query.mongodb.net/sample_mflix?ssl=true&authSource=admin"
    DB_NAME = "sample_mflix"
    DB_USER = " ezra54311_db_user"
    DB_PASSWORD = "MongoDatabase4Ezra"

    def __init__(self):
        pass


    def get_db_url(self):
        return self.URL
    
    def get_db_name(self):
        return self.DB_NAME
    def get_db_user(self):
        return self.DB_USER
    def get_db_password(self):
