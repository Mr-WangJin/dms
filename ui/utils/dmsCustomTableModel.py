import typing

from PyQt5 import Qt
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt

from ui.utils.dmsCustomData import DMSCustomData


class DMSCustomTableModel(QAbstractTableModel):
    customData: DMSCustomData = None

    def __init__(self, parent=None):
        super(DMSCustomTableModel, self).__init__(parent)

    def setCustomData(self, customData: DMSCustomData):
        self.customData = customData

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            return 1
        pass

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            return "列名"
        return super(DMSCustomTableModel, self).headerData(section, orientation, role)

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        pass

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return 1
        if self.customData is None:
            return 0
        return self.customData.rowCount()

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 2
        if self.customData is None:
            return 0
        return self.customData.columnCount()
