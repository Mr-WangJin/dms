# Custom表显示数据类
import typing

from sqlalchemy.testing.schema import Table

from bll.dmsContext import dmsDatabase, isProjectNull


class DMSCustomData(object):
    table = None
    recordList: typing.List = []
    metaTable = None

    def __init__(self):
        pass

    def setDisplayTable(self, table):
        self.table = table
        if isProjectNull():
            return
        self.recordList = dmsDatabase().getTableList()
        self.metaTable = dmsDatabase().getMetadata()
        self.metaTable = dmsDatabase().getTableMetadata()

    def rowCount(self) -> int:
        if self.table is None:
            return 0
        return self.recordList.count()

    def columnCount(self) -> int:
        pass

    def data(self, row: int, column: int) -> typing.Any:
        self.recordList[row]
        pass

    def setData(self):
        pass
