# encoding: utf-8
# 单元界面
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTabWidget, QToolBar, QAction, QVBoxLayout, QTableWidget, QHBoxLayout, QLabel, \
    QPushButton, QSpacerItem, \
    QSizePolicy, QToolButton, QButtonGroup
from PyQt5.sip import delete

from bll.dmsBusiness import *
from bll.dmsContext import dmsProject, isProjectNull, dmsDatabase
from dal.dmsTables import *
from ui.dmsDecorateType import DMSDecorateTypeWgt
from ui.ui_unitWgt import *
from ui.dmsDecorateData import *


class DMSUnitWgt(QWidget):
    unitTabDataWdg = None
    decorateTypeWgt: DMSDecorateTypeWgt = None
    decorateDataWgt: DMSDecorateDataWgt = None

    currentBuilding: DB_Building = None
    unitDict: dict = {}

    def __init__(self, parent=None):
        super(DMSUnitWgt, self).__init__(parent)

        self.initUI()
        self.initTrigger()

    def initUI(self):
        self.ui = Ui_UnitWgt()
        self.ui.setupUi(self)
        self.decorateTypeWgt = DMSDecorateTypeWgt(self)
        self.decorateDataWgt = DMSDecorateDataWgt(self)
        count = self.ui.verticalLayout.count()
        self.ui.verticalLayout.addWidget(self.decorateDataWgt)
        self.groupButton = QButtonGroup(self)
        self.groupButton.buttonClicked.connect(self.unitChanged)

    def unitChanged(self):
        self.decorateDataWgt.

    def initTrigger(self):
        self.ui.pBtnAddUnit.clicked.connect(self.addUnit)
        self.ui.pBtnDleleteUnit.clicked.connect(self.deleteUnit)

    def setCurrentBuilding(self, building_id):
        if self.currentBuilding and self.currentBuilding.id == building_id:
            return
        self.currentBuilding = None
        building: DB_Building = dmsDatabase().getRecordById(DB_Building, building_id)
        if building is None:
            self.updateUiEnabled()
            return
        self.currentBuilding = building
        self.clearUnit()
        self.loadUnit()
        self.updateUiEnabled()

    def getCurrentUnit(self):
        

    def addUnit(self):
        unit = newUnit(self.currentBuilding)
        unit_tool_btn = self.createToolButton(unit)
        unit_tool_btn.setChecked(True)

    def deleteUnit(self):
        _id = self.groupButton.checkedId()
        _button = self.groupButton.checkedButton()

        self.groupButton.removeButton(_button)
        delete(_button)
        customDeleteRecord(DB_Building_Unit, _id)
        self.updateUiEnabled()

    def createToolButton(self, business_unit) -> QToolButton:
        if business_unit is None:
            return
        unit_tool_btn = QToolButton()
        unit_tool_btn.setText(business_unit.name)
        unit_tool_btn.setCheckable(True)
        count = self.ui.horizontalLayout.count()
        self.ui.horizontalLayout.insertWidget(count - 3, unit_tool_btn)
        self.unitDict[business_unit.id] = unit_tool_btn
        self.groupButton.addButton(unit_tool_btn, business_unit.id)

        return unit_tool_btn

    def loadUnit(self):
        if self.currentBuilding is None:
            return
        unit_list = dmsDatabase().getTableList(DB_Building_Unit, "building_id = " + str(self.currentBuilding.id))
        if len(unit_list) == 0:
            return
        first_item: QToolButton = None
        for item in unit_list:
            unit_tool_btn = self.createToolButton(item)
            if first_item is None:
                first_item = unit_tool_btn
        first_item.setChecked(True)

    def clearUnit(self):
        if len(self.unitDict) == 0:
            return
        tool_btn_list = self.unitDict.values()

        for var in self.groupButton.buttons():
            self.groupButton.removeButton(var)

        for item in tool_btn_list:
            self.ui.horizontalLayout.removeWidget(item)
            delete(item)
        self.unitDict.clear()

    def updateUnitDate(self, currentBuildingID, previousBuildingID=None):
        """
        槽函数
        :param currentBuildingID:
        :param previousBuildingID:
        :return:
        """
        pass
        # # Todo 待梳理嵌套关系
        # print(currentBuildingID, previousBuildingID)
        # dateTableWidget = self.unitTabWdg.currentWidget()
        # dateTableWidget = DMSDecorateDataWgt()
        # # decorateTaskList: List[DB_Decorate_Type] = dmsProject().getTableList(DB_Decorate_Type, filter_str=currentBuildingID).orderBy(
        # #     DB_Decorate_Type.order)
        # decorateTaskList: List[DB_Decorate_Type] = dmsDatabase().getTableList(DB_Decorate_Type)
        # tableHeaderList = [task.name for task in decorateTaskList]
        # dateTableWidget.setHorizontalHeaderLabels(tableHeaderList)

    def updateUiEnabled(self):
        enabled = False
        if len(self.unitDict) == 0:
            enabled = False
        else:
            enabled = True

        self.ui.pBtnDleleteUnit.setEnabled(enabled)

