# coding=utf-8
from bll.dmsContext import glb_dmsContext
from dal.dmsDatabase import DMSDatabase


def newDMSProject(file_name):
    database = DMSDatabase()
    database.newDatabase(file_name)
    project = DMSProject(database)
    glb_dmsContext.setProject(project)


def openDMSProject(file_name):
    database = DMSDatabase()
    database.openDatabase(file_name)
    glb_dmsContext.setProject(DMSProject(database))


class DMSProject(object):
    dmsDatabase = None

    def __init__(self, database):
        self.dmsDatabase = database

