# encoding: utf-8
# 单元界面
from PyQt5.QtWidgets import QWidget, QTabWidget, QToolBar, QAction, QVBoxLayout, QTableWidget

from ui.dmsDecorateDataWgt import DMSDecorateDataWgt


class DMSUnitWgt(QWidget):
    unitTabWdg = None
    unitTabDataWdg = None

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
        self.initUI()
        self.initTrigger()
        # 创建3个选项卡小控件窗口
        # self.tab1 = QWidget()
        # self.tab2 = QWidget()
        # self.tab3 = QWidget()

        # self.addTab(self.tab1, "Tab 1")
        # self.addTab(self.tab2, "Tab 2")
        # self.addTab(self.tab3, "Tab 3")

    def initUI(self):
        self.tooBar.addAction(self.actAddUnit)
        self.tooBar.addAction(self.actDelUnit)
        self.tooBar.addAction(self.actAddFloor)
        self.tooBar.addAction(self.actDelFloor)
        self.tooBar.addAction(self.actAddRoom)
        self.tooBar.addAction(self.actDelRoom)
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

    def addUnit(self):
        self.unitTabDataWdg = DMSDecorateDataWgt()
        currentTabIndex = self.unitTabWdg.currentIndex()
        self.unitTabWdg.insertTab(currentTabIndex, self.unitTabDataWdg, "单元1")

    def delUnit(self):
        currentTabIndex = self.unitTabWdg.currentIndex()
        self.unitTabWdg.removeTab(currentTabIndex)

    def updateUnitDate(self):
        # Todo 待梳理嵌套关系
        # dateTableWidget: DMSDecorateDataWgt = self.unitTabWdg.currentWidget()
        # dateTableWidget.layout().removeWidget(0)
        # layout = QVBoxLayout()
        # tableWdg = QTableWidget()
        # layout.addWidget(tableWdg)
        pass
