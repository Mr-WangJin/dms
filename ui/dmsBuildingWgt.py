# encoding: utf-8
# module ui



from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from bll.dmsContext import dms_context
from dal.dmsTables import DB_Building
from ui.ui_wgtBuilding import Ui_wgtBuilding


class DMSBuildingWgt(QWidget):
    def __init__(self, parent=None):
        super(DMSBuildingWgt, self).__init__(parent)
        self.ui = Ui_wgtBuilding()
        self.ui.setupUi(self)

        self.ui.toolBtnAdd.clicked.connect(self.addNewBuilding)

    def updateBuilding(self):
        self.ui.treeWidget.clear()
        project = dms_context.getProject()
        buildingList = project.getTableList(DB_Building)

        for building in buildingList:
            item = QTreeWidgetItem()
            item.setText(0, building.name)
            self.ui.treeWidget.addTopLevelItem(item)


    def addNewBuilding(self):
        building = DB_Building()
        building.name = "测试新建单体"
        building.order = 0

        dms_context.getProject().addRecord(building)

        self.updateBuilding()






