# 数据库类
from typing import List

import sqlalchemy as sa
from PyQt5.QtWidgets import QAction
from sqlalchemy import MetaData, text, func
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
    metadata: MetaData = None

    # BASE_PATH = "sqlite:///sochi_athletes.sqlite3"

    def __init__(self):
        pass

    def getSession(self):
        return self.session

    def getTableMetadata(self, table_str):
        # 反射表
        meta_table = Table(table_str, self.metadata, autoload=True, autoload_with=self.__engine__)
        return meta_table

    # 打开数据库
    def openDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.__engine__ = sa.create_engine(sqlite_file_name)
        # Base.metadata.create_all(self.__engine__)
        db_session = sessionmaker(bind=self.__engine__)
        self.session = db_session()
        self.metadata = MetaData(bind=self.__engine__)

    # 新建数据库
    def newDatabase(self, filename):
        self.fileName = filename
        sqlite_file_name = "sqlite:///" + self.fileName
        self.__engine__ = sa.create_engine(sqlite_file_name)
        Base.metadata.create_all(self.__engine__)
        db_session = sessionmaker(bind=self.__engine__)
        self.session = db_session()
        self.metadata = MetaData(bind=self.__engine__)

        print("新建数据库")

    def closeDatabase(self):
        pass

    # 获取数据库版本
    def dbVersion(self):
        pass

    def getTableList(self, table, filter_str: str = '') -> List:
        """

        :param table: 获取表记录
        :param filter_str: 过滤条件
        :return:
        """
        if filter_str is None:
            table_list = self.session.query(table).all()
            return table_list
        # table_list = self.session.query(table).filter(filter_str).one_or_none()
        table_list = self.session.query(table).filter(text(filter_str)).all()
        return table_list

    def getTableRecordCount(self, table, _filter) -> int:
        count = self.session.query(table).filter(text(_filter)).count()
        return count + 1

    def getRecordById(self, table, _id):
        item = self.session.query(table).filter_by(id=_id).one_or_none()
        return item

    def getMaxOrder(self, table) -> int:
        max_int = 1
        items = self.session.query(func.max(table.order)).all()
        if items is None or len(items) <= 1:
            return max_int
        return items[0].order

    def getCount(self, table: Base):
        return self.session.query(table).count()
        # item = self.session.query(table).from_statement(text("select max(order) from "+table.____tablename__+"")).one_or_none()

    # 添加记录
    def addRecord(self, record):
        if record is None or self.session is None:
            return 0
        self.session.add(record)
        self.commit()
        return True

    # 更新记录
    def updateRecord(self, filter: str, record):
        if record is None or self.session is None:
            return 0
        org = self.session.query(type(record)).filter(text(filter)).update()

        self.commit()

    # 删除记录
    def deleteRecord(self, record) -> bool:
        if record is None or self.session is None:
            return False
        self.session.delete(record)
        self.commit()
        return True

    def deleteRecordByID(self, table, id):
        if id:
            self.session.query(table).filter(id == id).delete()

    # 提交
    def commit(self):
        self.session.commit()

    # 撤销
    def rollback(self):
        self.session.rollback()

    def getMetadata(self):
        return Base.metadata
