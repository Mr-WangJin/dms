
#工程类

from bll.dmsContext import dms_context
from dal.dmsDatabase import DMSDatabase


# 新建工程
def newProject(fileName):
	database = DMSDatabase()
	database.openDatabase(fileName)
	dms_context.setProject(DMSProject(database))


# 打开工程
def openProject(fileName):
	pass


# 打开工程
def openProject(self, fileName):
	pass


class DMSProject(object):

	dmsDatabase = None
	
	def __init__(self, database):
		self.dmsDatabase = database


	def getTableList(self, table):
		return dmsDatabase.session.query(table).all()



		


