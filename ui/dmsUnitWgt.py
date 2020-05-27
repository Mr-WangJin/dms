# encoding: utf-8
# 单元界面
from typing import List

from PyQt5.QtWidgets import QWidget, QTabWidget, QToolBar, QAction, QVBoxLayout, QTableWidget

from bll.dmsContext import dmsProject, isProjectNull, dmsDatabase
from dal.dmsTables import DB_Decorate_Type
from ui.dmsDecorateDataWgt import DMSDecorateDataWgt
from ui.dmsDecorateType import DMSDecorateTypeWgt


class DMSUnitWgt(QWidget):
    unitTabWdg = None
    unitTabDataWdg = None
    decorateTypeWgt = None

    def __init__(self, parent=None):
        super(DMSUnitWgt, self).__init__(parent)
        self.tooBar = QToolBar("UnitToolBar")
        self.unitTabWdg = QTabWidget()
        self.actAddUnit = QAction("插入单元")
        self.actDelUnit = QAction("删除单元")
        self.actAddFloor = QAction("插入楼层")
        self.actDelFloor = QAction("删除楼层")
        self.actAddRoom = QAction("插入户型")
        self.actDelRoom = QAction("删除户型")
        self.actEditTask = QAction("编辑计划")
        self.initUI()
        self.initTrigger()

    def initUI(self):
        self.tooBar.addAction(self.actAddUnit)
        self.tooBar.addAction(self.actDelUnit)
        self.tooBar.addSeparator()
        self.tooBar.addAction(self.actAddFloor)
        self.tooBar.addAction(self.actDelFloor)
        self.tooBar.addAction(self.actAddRoom)
        self.tooBar.addAction(self.actDelRoom)
        self.tooBar.addSeparator()
        self.tooBar.addAction(self.actEditTask)
        layout = QVBoxLayout()
        layout.addWidget(self.tooBar)
        layout.addWidget(self.unitTabWdg)
        self.setLayout(layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.unitTabWdg.setMovable(True)

    def initTrigger(self):
        self.actAddUnit.triggered.connect(self.addUnit)
        self.actDelUnit.triggered.connect(self.delUnit)
        self.actEditTask.triggered.connect(self.parent().editTask)



    def addUnit(self):
        self.unitTabDataWdg = DMSDecorateDataWgt()
        currentTabIndex = self.unitTabWdg.currentIndex()
        self.unitTabWdg.insertTab(currentTabIndex, self.unitTabDataWdg, "单元1")

    def delUnit(self):
        currentTabIndex = self.unitTabWdg.currentIndex()
        self.unitTabWdg.removeTab(currentTabIndex)

    def updateUnitDate(self, currentBuildingID, previousBuildingID=None):
        """
        槽函数
        :param currentBuildingID:
        :param previousBuildingID:
        :return:
        """

        # Todo 待梳理嵌套关系
        print(currentBuildingID, previousBuildingID)
        dateTableWidget = self.unitTabWdg.currentWidget()
        dateTableWidget = DMSDecorateDataWgt()
        # decorateTaskList: List[DB_Decorate_Type] = dmsProject().getTableList(DB_Decorate_Type, filter_str=currentBuildingID).orderBy(
        #     DB_Decorate_Type.order)
        decorateTaskList: List[DB_Decorate_Type] = dmsDatabase().getTableList(DB_Decorate_Type)
        tableHeaderList = [task.name for task in decorateTaskList]
        dateTableWidget.setHorizontalHeaderLabels(tableHeaderList)

    def updateUiEnabled(self):
        enabled = False if isProjectNull() else True
        for act in self.tooBar.actions():
            act.setEnabled(enabled)
