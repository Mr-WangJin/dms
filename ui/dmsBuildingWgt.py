# encoding: utf-8
# module ui
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QAbstractItemView, QAction
from sqlalchemy import MetaData

from bll.dmsContext import *
from dal.dmsTables import *
from ui.ui_wgtBuilding import Ui_wgtBuilding
from dal.dmsDatabase import *


class DMSBuildingWgt(QWidget):
    currentItem: QTreeWidgetItem = None

    def __init__(self, parent=None):
        super(DMSBuildingWgt, self).__init__(parent)
        self.ui = Ui_wgtBuilding()
        self.actMoveUp = QAction("上移")
        self.initUI()
        self.initTrigger()

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.AnyKeyPressed)
        self.setStyleSheet("QWidget::Item{}")
        self.setFixedWidth(320)

    def initTrigger(self):
        self.ui.toolBtnAdd.clicked.connect(self.addNewBuilding)
        self.ui.toolBtnDelete.clicked.connect(self.deleteBuilding)
        self.ui.treeWidget.currentItemChanged.connect(self.parent().buildingChanged)

    # 刷新单体树
    def updateBuilding(self):
        """
        刷新单体
        :return:
        """
        self.ui.treeWidget.clear()
        building_list = dmsDatabase().getTableList(DB_Building)

        # rootItem = QTreeWidgetItem()
        # rootItem.setHidden(True)
        building: DB_Building
        for building in building_list:
            item = QTreeWidgetItem()
            item.setText(0, building.name)
            item.setData(0, Qt.UserRole, building)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            # rootItem.addChild(item)
            self.ui.treeWidget.addTopLevelItem(item)
        firstItem = self.ui.treeWidget.topLevelItem(0)
        if firstItem is not None:
            firstItem.setSelected(True)

    # 获取当前单体
    def getCurrentBuilding(self):
        item: QTreeWidgetItem = self.ui.treeWidget.currentItem()
        pass

    def addNewBuilding(self):
        building = DB_Building()
        building.name = "测试新建单体"
        building.order = 0
        dmsDatabase().addRecord(building)

        self.updateBuilding()
        #
        # meta: MetaData = dmsDatabase().getMetadata()
        # for var in meta.tables:
        #     print(var)
        # aa = DB_Building.metadata

    def deleteBuilding(self):
        item: QTreeWidgetItem = self.ui.treeWidget.currentItem()
        if not item:
            return
        cur_building = item.data(0, Qt.UserRole)
        dmsDatabase().deleteRecord(cur_building)
        index: QModelIndex = self.ui.treeWidget.currentIndex()
        self.ui.treeWidget.takeTopLevelItem(index.row())

        # self.updateBuilding()

    def updateUiEnabled(self):
        """
        解除页面按钮禁用状态，当未创建工程时。
        :return:
        """
        enabled = isProjectNull()
        enabled = not enabled
        self.ui.toolBtnAdd.setEnabled(enabled)
        self.ui.toolBtnDelete.setEnabled(enabled)
