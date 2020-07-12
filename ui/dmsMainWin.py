# encoding: utf-8
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHBoxLayout, QVBoxLayout, QAction, QToolBar, QTreeWidgetItem, QSplitter

from bll import dmsBusiness
from bll.dmsProject import *
from ui.nodeeditor.NodeEditerWidget.NodeEditorWidget import NodeEditorWidget
from ui.dmsBuildingWgt import DMSBuildingWgt, isProjectNull
from ui.dmsDecorateType import DMSDecorateTypeWgt
from ui.dmsUnitWgt import DMSUnitWgt
from ui.ui_mainWin import Ui_MainWindow


class DMSMainWin(QMainWindow):
    WIDGET_SPACING = 4
    BUILDINGWGT_WIDTH = 320
    UNITTABWGT_WIDTH = 400
    NODEWGT_WIDTH = 400
    horizonlayout = None
    buildingWgt = None
    unitTabWgt = None
    nodeViewWgt = None
    ribbonBanner = None
    decorateTypeWgt = None

    def __init__(self, parent=None):
        super(DMSMainWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('装修管理')
        self.ui.actNewProject.triggered.connect(self.newProject)
        self.ui.actOpenProject.triggered.connect(self.openProject)
        self.toolBar = self.addToolBar("工具栏")
        # self.actNewProject = QAction("新建工程")
        self.initUi()
        self.initTrigger()
        newDMSProject('./tmpProject/' + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + 'dms')
        self.updateUiEnabled()

    def initTrigger(self):
        '''切换单体'''
        # self.buildingWgt.ui.treeWidget.currentChanged.connect(self.unitTabWgt.updateUnitDate)
        pass

    def newProject(self):
        new_file = QFileDialog().getSaveFileName(None, '新建工程', '', '*.dms')
        if new_file[0] == "":
            return False
        else:
            newDMSProject(new_file[0])
            self.updateUiEnabled()
            return True

    def openProject(self):
        open_file = QFileDialog().getOpenFileName(None, '打开工程', '', '*.dms')
        if open_file[0] == "":
            return False
        openDMSProject(open_file[0])
        self.buildingWgt.updateBuildingList()
        self.updateUiEnabled()
        return True

    def initUi(self):
        '''页面整体布局'''

        '''building widget'''
        self.buildingWgt = DMSBuildingWgt(self)
        self.buildingWgt.sigBuildingChanged.connect(self.buildingChanged)
        self.buildingWgt.setFixedWidth(DMSMainWin.BUILDINGWGT_WIDTH)

        '''unit widget'''
        self.unitWgt = DMSUnitWgt(self)
        self.unitWgt.setMinimumWidth(DMSMainWin.UNITTABWGT_WIDTH)

        '''node widget'''
        self.nodeViewWgt = NodeEditorWidget(self)
        self.nodeViewWgt.setMinimumWidth(DMSMainWin.NODEWGT_WIDTH)

        '''right spliter'''
        self.rightSpliter = QSplitter(Qt.Horizontal)
        self.rightSpliter.addWidget(self.nodeViewWgt)
        self.rightSpliter.addWidget(self.unitWgt)
        self.rightSpliter.setStretchFactor(0, 1)
        self.rightSpliter.setStretchFactor(1, 1)

        '''主水平布局'''
        self.horizonlayout = QHBoxLayout(self)
        self.horizonlayout.setAlignment(Qt.AlignLeft)
        self.horizonlayout.setContentsMargins(0, 0, 0, 0)
        self.horizonlayout.setSpacing(DMSMainWin.WIDGET_SPACING)

        self.horizonlayout.addWidget(self.buildingWgt)
        self.horizonlayout.addWidget(self.rightSpliter)
        self.horizonlayout.setStretch(0, 1)
        self.horizonlayout.setStretch(1, 4)
        self.centralWidget().setLayout(self.horizonlayout)
        self.unitWgt.setVisible(False)
        self.nodeViewWgt.setVisible(False)
        '''工具栏'''
        self.toolBar.setFixedHeight(glb_dmsContext.TOOLBAR_HEIGHT)
        self.toolBar.addAction(self.ui.actNewProject)
        self.toolBar.addAction(self.ui.actOpenProject)
        self.toolBar.setMovable(False)
        self.updateUiEnabled()
        '''设置全局样式'''
        # self.ui.centralwidget.layout().addWidget(self.ribbonBanner)
        '''单体列表'''
        self.setStyleSheet("QTreeWidget::item{height:40px}")
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def updateUiEnabled(self):
        self.buildingWgt.updateUiEnabled()
        self.unitWgt.updateUiEnabled()
        self.unitWgt.setVisible(not isProjectNull())
        self.nodeViewWgt.setVisible(not isProjectNull())

    def buildingChanged(self, current_id, previous_id):
        # self.unitWgt.updateUnitDate(current, previous)

        self.unitWgt.setCurrentBuilding(current_id)

    # 接受各组件信号
    def editTask(self):
        self.decorateTypeWgt = DMSDecorateTypeWgt()
        self.decorateTypeWgt.showNormal()

    def updateUnitTabWgd(self, current, previous):
        # self.unitTabWgt.updateUnitDate(current, previous)
        pass
