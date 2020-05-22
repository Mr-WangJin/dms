# 数据库类

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


class DMSDatabase(object):
    session = None
    engine = None
    fileName = ""
    #BASE_PATH = "sqlite:///sochi_athletes.sqlite3"

    def __init__(self):
        pass

    # 打开数据库
    def openDatabase(self, fileName):
        engine = sa.create_engine(fileName)
        # Base.metadata.create_all(engine)
        dbSession = sessionmaker(bind=engine)
        session = dbSession()

    def closeDatabase(self):
        pass

    # 获取数据库版本
    def dbVersion(self):
        pass

    # 
    def getTableList(self, tableName, filter):
        pass

    def session(self):
        return self.session

