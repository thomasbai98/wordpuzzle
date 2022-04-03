class config:
    def __init__(self):
        self.__secret_key = (b'n\x7f\x0b\xd2\xaf5Zp\xb9\xa6R\x16'
                            b'\xe29\xe8\xf3\xba\xe7j\xf9I%]\xb3')
        DB_NAME = "userinfo.db" 
        self.__dbname = DB_NAME 
        self.__URI = f'sqlite:///{DB_NAME}'
        self.__track = False
        db_type = "postgresql+psycopg2"
        username = "Yuyang"
        pw = "Byy_19981201"
        endpoint = "aaopjq5i1gu2pm.c3vzkbqj91vt.us-east-1.rds.amazonaws.com"
        port = "5432"
        engine = "postgres"
        self.__rdsURI = f'{db_type}://{username}:{pw}@{endpoint}:{port}/{engine}'
    def get_secret_key(self):
        return self.__secret_key
    def get_dbname(self):
        return self.__dbname
    def get_uri(self):
        return self.__URI
    def get_RDSuri(self):
        return self.__rdsURI
    def get_track(self):
        return self.__track