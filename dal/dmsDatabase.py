# 数据库类

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from dal.dmsTables import *


class DMSDatabase(object):
    session = None
    engine = None
    fileName = ""

    # BASE_PATH = "sqlite:///sochi_athletes.sqlite3"

    def __init__(self):
        pass

    # 打开数据库
    def openDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.engine = sa.create_engine(sqlite_file_name)
        # Base.metadata.create_all(engine)
        dbSession = sessionmaker(bind=self.engine)
        self.session = dbSession()


    #新建数据库
    def newDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.engine = sa.create_engine(sqlite_file_name)
        Base.metadata.create_all(self.engine)
        db_session = sessionmaker(bind=self.engine)
        self.session = db_session()

    def closeDatabase(self):
        pass

    # 获取数据库版本
    def dbVersion(self):
        pass

    # 
    def getTableList(self, tableName, filter):
        pass

    def getSession(self):
        return self.session

    # 添加记录
    def addRecord(self, record):
        if record == None or self.session == None:
            return 0
        self.session.add(record)
        self.session.commit()

    # 删除记录
    def deleteRecord(self, record):
        if record == None or self.session == None:
            return 0
        self.session.delete(record)
        self.session.commit()



