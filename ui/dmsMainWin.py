# encoding: utf-8


from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHBoxLayout, QVBoxLayout

from bll.dmsProject import *
from nodeeditor.NodeEditerWidget.NodeEditorWidget import NodeEditorWidget
from ui.dmsBuildingWgt import DMSBuildingWgt
from ui.dmsUnitWgt import DMSUnitWgt
from ui.ui_mainWin import Ui_MainWindow


class DMSMainWin(QMainWindow):
    WIDGET_SPACING = 4
    BUILDINGWGT_WIDTH = 240
    UNITTABWGT_WIDTH = 400
    NODEWGT_WIDTH = 400
    horizonlayout = None
    buildingWgt = None
    unitTabWgt = None
    nodeViewWgt = None

    def __init__(self, parent=None):
        super(DMSMainWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('装修管理')
        self.ui.actNewProject.triggered.connect(self.newProject)
        self.ui.actOpenProject.triggered.connect(self.openProject)

        self.initUi()

    def newProject(self):
        new_file = QFileDialog().getSaveFileName(None, '新建工程', '', '*.dms')
        if new_file[0] == "":
            return False

        newDMSProject(new_file[0])
        self.updateUiEnabled()
        return True

    def openProject(self):
        open_file = QFileDialog().getOpenFileName(None, '打开工程', '', '*.dms')
        if open_file[0] == "":
            return False
        openDMSProject(open_file[0])
        self.buildingWgt.updateBuilding()
        self.updateUiEnabled()
        return True

    def initUi(self):
        self.horizonlayout = QHBoxLayout(self)
        self.horizonlayout.setContentsMargins(0, 0, 0, 0)
        self.horizonlayout.setSpacing(DMSMainWin.WIDGET_SPACING)

        self.buildingWgt = DMSBuildingWgt(self)
        self.buildingWgt.setFixedWidth(DMSMainWin.BUILDINGWGT_WIDTH)
        self.unitTabWgt = DMSUnitWgt(self)
        self.unitTabWgt.setMinimumWidth(DMSMainWin.UNITTABWGT_WIDTH)
        self.nodeViewWgt = NodeEditorWidget(self)
        self.nodeViewWgt.setMinimumWidth(DMSMainWin.NODEWGT_WIDTH)

        self.horizonlayout.addWidget(self.buildingWgt)
        self.horizonlayout.addWidget(self.unitTabWgt)
        self.horizonlayout.addWidget(self.nodeViewWgt)

        self.horizonlayout.setStretch(0, 0)
        self.horizonlayout.setStretch(1, 1)
        self.horizonlayout.setStretch(2, 1)
        self.centralWidget().setLayout(self.horizonlayout)

        self.updateUiEnabled()

    def updateUiEnabled(self):
        self.buildingWgt.updateUiEnabled()
