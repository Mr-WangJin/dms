# 数据库类

import sqlalchemy as sa
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.schema import *
from sqlalchemy.engine import Engine
from dal.dmsTables import *
from sqlalchemy.orm import *


# def getMetadata():
#     return MetaData(bind=db)


class DMSDatabase(object):
    session: Session = None
    __engine__: Engine = None
    fileName: String = ""

    # BASE_PATH = "sqlite:///sochi_athletes.sqlite3"

    def __init__(self):
        pass

    def getSession(self):
        return self.session

    # 打开数据库
    def openDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.__engine__ = sa.create_engine(sqlite_file_name)
        # Base.metadata.create_all(self.__engine__)
        db_session = sessionmaker(bind=self.__engine__)
        self.session = db_session()

    # 新建数据库
    def newDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.__engine__ = sa.create_engine(sqlite_file_name)
        Base.metadata.create_all(self.__engine__)
        db_session = sessionmaker(bind=self.__engine__)
        self.session = db_session()

    def closeDatabase(self):
        pass

    # 获取数据库版本
    def dbVersion(self):
        pass

    # 获取表记录
    # @filter_str ： 过滤条件
    def getTableList(self, table, filter_str=None):
        if filter_str is None:
            table_list = self.session.query(table).all()
            return table_list
        # table_list = self.session.query(table).filter(filter_str).one_or_none()
        table_list = self.session.query(table).filter(filter_str)
        return table_list

    # 添加记录
    def addRecord(self, record):
        if record is None or self.session is None:
            return 0
        self.session.add(record)
        self.session.commit()

    # 更新记录
    def updateRecord(self, tableName, record):
        filterName, filterValue, columnName, value = record
        self.session.query(tableName).filter_by(filterName=filterValue).update({columnName: value})
        self.session.commit()

    # 删除记录
    def deleteRecord(self, record):
        if record is None or self.session is None:
            return 0
        self.session.delete(record)
        self.session.commit()

    # 提交
    def commit(self):
        self.session.commit()

    # 撤销
    def rollback(self):
        self.session.rollback()

    def getMetadata(self):
        return Base.metadata
