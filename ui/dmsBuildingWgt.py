# encoding: utf-8
# module ui

from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QAbstractItemView, QAction
from sqlalchemy import MetaData

from bll import dmsBusiness
from bll.dmsBusiness import *
from bll.dmsContext import *
from ui.ui_wgtBuilding import Ui_wgtBuilding
from dal.dmsDatabase import *
from PyQt5.QtCore import QObject, pyqtSignal


class DMSBuildingWgt(QWidget):
    currentItem: QTreeWidgetItem = None

    sigBuildingChanged = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(DMSBuildingWgt, self).__init__(parent)
        self.ui = Ui_wgtBuilding()

        self.actMoveUp = QAction("上移")
        self.initUI()
        self.initTrigger()
        # self.ui.treeWidget.currentItemChanged.connect(self.buildingChanged)

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.treeWidget.setColumnCount(3)
        self.ui.treeWidget.setColumnHidden(0, True)
        self.ui.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.AnyKeyPressed)
        self.setStyleSheet("QWidget::Item{}")
        self.setFixedWidth(320)

    def initTrigger(self):
        self.ui.toolBtnAdd.clicked.connect(self.insertBuilding)
        self.ui.toolBtnDelete.clicked.connect(self.deleteBuilding)
        # self.ui.treeWidget.currentItemChanged.connect(self.parent().buildingChanged)
        self.ui.treeWidget.itemChanged.connect(self.updateBuilding)

    def buildingChanged(self, current, previous):
        if previous is None and current is None:
            self.sigBuildingChanged.emit(-1, -1)
        elif current is None:
            pre_building = previous.data(0, Qt.UserRole)
            self.sigBuildingChanged.emit(-1, pre_building.id)
        elif previous is None:
            cur_building = current.data(0, Qt.UserRole)
            self.sigBuildingChanged.emit(cur_building.id, -1)
        else:
            cur_building = current.data(0, Qt.UserRole)
            pre_building = previous.data(0, Qt.UserRole)
            self.sigBuildingChanged.emit(cur_building.id, pre_building.id)
        # ws
        # cur = current.data(0, Qt.UserRole).id if current else -1
        # pre = previous.data(0, Qt.UserRole).id if previous else -1
        # self.sigBuildingChanged.emit(cur, pre)

    def updateBuildingList(self):
        """
        刷新单体列表的内容
        :return:
        """
        self.ui.treeWidget.clear()
        building_list: List[DB_Building] = dmsDatabase().getTableList(DB_Building)

        # rootItem = QTreeWidgetItem()
        # rootItem.setHidden(True)
        for building in building_list:
            item = self.building2Item(building)
            # rootItem.addChild(item)
            self.ui.treeWidget.addTopLevelItem(item)
        firstItem = self.ui.treeWidget.topLevelItem(0)
        if firstItem is not None:
            firstItem.setSelected(True)

    # item building 互转 =============================================================
    def building2Item(self, building: DB_Building) -> QTreeWidgetItem:
        item = QTreeWidgetItem()
        item.setText(0, building.id.__str__())
        item.setText(1, building.name)
        item.setText(2, building.order.__str__())
        # item.setData(0, Qt.UserRole, building)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
        return item

    def item2Building(self, item):
        id = item.text(0)
        name = item.text(1)
        order = item.text(2)
        return DB_Building(id=id, name=name, order=order)

    # 获取当前单体
    def getCurrentBuilding(self) -> DB_Building:
        item: QTreeWidgetItem = self.ui.treeWidget.currentItem()
        building = item.data(0, Qt.UserRole)
        return building

    # CRUD  ======================================================
    def insertBuilding(self):
        selectedItems = self.ui.treeWidget.selectedItems()
        count = self.ui.treeWidget.topLevelItemCount()
        currentRow = self.ui.treeWidget.indexOfTopLevelItem(selectedItems[0]) if len(selectedItems) > 0 else count
        building = dmsBusiness.newBuilding(0)
        item = self.building2Item(building)
        row = currentRow + 1 if currentRow < count else count
        self.ui.treeWidget.insertTopLevelItem(row, item)
        self.updateBuildingOrder(row)
        self.ui.treeWidget.setCurrentItem(item)
        # self.updateUiEnabled()

    def deleteBuilding(self):
        item: QTreeWidgetItem = self.ui.treeWidget.currentItem()
        if not item:
            return
        cur_building = self.item2Building(item)
        dmsDatabase().deleteRecordByID(DB_Building, cur_building)
        index: QModelIndex = self.ui.treeWidget.currentIndex()
        self.ui.treeWidget.takeTopLevelItem(index.row())
        self.updateBuildingOrder(index.row())

    def updateBuilding(self, item: QTreeWidgetItem, column):
        row = self.ui.treeWidget.indexOfTopLevelItem(item)
        building = DB_Building(id=item.text(0), name=item.text(1), order=item.text(2))
        dmsBusiness.updateBuilding(building)

    def updateBuildingOrder(self, startRow):
        for index in range(startRow, self.ui.treeWidget.topLevelItemCount()):
            item = self.ui.treeWidget.topLevelItem(index)
            item.setData(2, Qt.DisplayRole, index)
            print(index, item.text(0), item.text(1), item.text(2))
            building = self.item2Building(item)
            dmsBusiness.updateBuilding(building)

    def updateUiEnabled(self):
        """
        解除页面按钮禁用状态，当未创建工程时。
        :return:
        """
        enabled = isProjectNull()
        enabled = not enabled
        self.ui.toolBtnAdd.setEnabled(enabled)
        self.ui.toolBtnDelete.setEnabled(enabled)
