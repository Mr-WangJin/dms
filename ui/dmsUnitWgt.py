# encoding: utf-8
# 单元界面
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTabWidget, QToolBar, QAction, QVBoxLayout, QTableWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, \
    QSizePolicy

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
        '''顶部banner'''
        self.topBanner = QWidget(self)  # 顶部标题行
        self.bannerLayout = QHBoxLayout(self.topBanner)  # 顶部标题行布局
        self.bannerLabel = QLabel("单元列表")
        self.addUnitBtn = QPushButton("插入")
        self.delUnitBtn = QPushButton("删除")
        '''toolBar组件'''
        self.toolBar = QToolBar("UnitToolBar")
        self.actAddUnit = QAction("插入单元")
        self.actDelUnit = QAction("删除单元")
        self.actAddFloor = QAction("插入楼层")
        self.actDelFloor = QAction("删除楼层")
        self.actAddRoom = QAction("插入户型")
        self.actDelRoom = QAction("删除户型")
        self.actEditTask = QAction("编辑计划")
        '''tab组件'''
        self.unitTabWdg = QTabWidget(self)
        self.spacerItem = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.initUI()
        self.initTrigger()

    def initUI(self):
        '''组装部件'''
        layout = QVBoxLayout()
        layout.addWidget(self.topBanner)
        # layout.addWidget(self.toolBar)
        layout.addWidget(self.unitTabWdg)
        self.setLayout(layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        # topBanner
        self.bannerLayout.setContentsMargins(16, 0, 16, 0)
        self.topBanner.setFixedHeight(60)
        self.bannerLabel.setFont(QFont('单元列表', 20, 100))
        self.topBanner.setStyleSheet('QWidget {background-color:#ffffff;}')
        self.topBanner.layout().addWidget(self.bannerLabel)
        self.topBanner.layout().addItem(self.spacerItem)
        self.topBanner.layout().addWidget(self.addUnitBtn)
        self.addUnitBtn.setFixedHeight(60)
        self.addUnitBtn.setStyleSheet("QPushButton { border: none; }")
        self.topBanner.layout().addWidget(self.delUnitBtn)
        self.delUnitBtn.setFixedHeight(60)
        self.delUnitBtn.setStyleSheet("QPushButton { border: none; }")

        # toolBar
        # self.toolBar.addAction(self.actAddUnit)
        # self.toolBar.addAction(self.actDelUnit)
        # self.toolBar.addSeparator()
        self.toolBar.addAction(self.actAddFloor)
        self.toolBar.addAction(self.actDelFloor)
        self.toolBar.addAction(self.actAddRoom)
        self.toolBar.addAction(self.actDelRoom)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEditTask)

        self.unitTabWdg.setMovable(True)

    def initTrigger(self):
        self.actAddUnit.triggered.connect(self.addUnit)
        self.actDelUnit.triggered.connect(self.delUnit)
        self.addUnitBtn.clicked.connect(self.addUnit)
        self.delUnitBtn.clicked.connect(self.delUnit)
        self.actEditTask.triggered.connect(self.parent().editTask)

    def addUnit(self):
        self.unitTabDataWdg = DMSDecorateDataWgt()
        unitTabDataWdgLayout = QVBoxLayout(self.unitTabDataWdg)
        unitTabDataWdgLayout.setContentsMargins(0, 0, 0, 0)
        unitTabDataWdgLayout.setSpacing(0)
        unitTabDataWdgLayout.setAlignment(Qt.AlignTop)
        unitTabDataWdgLayout.addWidget(self.toolBar)
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
        for act in self.toolBar.actions():
            act.setEnabled(enabled)
