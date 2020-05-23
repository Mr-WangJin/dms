# 工程类
from bll.dmsContext import dms_context
from dal import dmsDatabase
from dal.dmsDatabase import DMSDatabase


def newDMSProject(file_name):
    database = DMSDatabase()
    database.newDatabase(file_name)
    dms_context.setProject(DMSProject(database))


def openDMSProject(file_name):
    database = DMSDatabase()
    database.openDatabase(file_name)
    dms_context.setProject(DMSProject(database))


class DMSProject(object):
    dmsDatabase = None

    def __init__(self, database):
        self.dmsDatabase = database

    def getTableList(self, table):
        table_list = self.dmsDatabase.session.query(table).all()
        return table_list

    def addRecord(self, record):
        if record == None:
            return 0
        self.dmsDatabase.addRecord(record)


