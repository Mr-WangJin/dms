# encoding: utf-8
# module ui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from bll.dmsContext import *
from dal.dmsTables import DB_Building
from ui.ui_wgtBuilding import Ui_wgtBuilding


class DMSBuildingWgt(QWidget):
    def __init__(self, parent=None):
        super(DMSBuildingWgt, self).__init__(parent)
        self.ui = Ui_wgtBuilding()
        self.ui.setupUi(self)

        self.ui.toolBtnAdd.clicked.connect(self.addNewBuilding)
        self.ui.toolBtnDelete.clicked.connect(self.deleteBuilding)

    # 刷新单体树
    def updateBuilding(self):
        self.ui.treeWidget.clear()
        buildingList = dmsProject().getTableList(DB_Building)

        building:DB_Building
        for building in buildingList:
            item = QTreeWidgetItem()
            item.setText(0, building.name)
            item.setData(0, Qt.UserRole, building)
            self.ui.treeWidget.addTopLevelItem(item)

    def getCurrentBuilding(self):
        pass


    def addNewBuilding(self):
        building = DB_Building()
        building.name = "测试新建单体"
        building.order = 0

        dmsDatabase().addRecord(building)

        self.updateBuilding()

    def deleteBuilding(self):
        item:QTreeWidgetItem = self.ui.treeWidget.currentItem()
        if item == None:
            return
        curBuilding = item.data(0, Qt.UserRole)
        dmsDatabase().deleteRecord(curBuilding)
        self.updateBuilding()







