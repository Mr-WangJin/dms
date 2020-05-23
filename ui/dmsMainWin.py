# encoding: utf-8


from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHBoxLayout, QVBoxLayout

from bll.dmsProject import *
from ui.dmsBuildingWgt import DMSBuildingWgt
from ui.ui_mainWin import Ui_MainWindow


class DMSMainWin(QMainWindow):

    horizonlayout = None
    buildingWgt = None

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
            return 0

        newDMSProject(new_file[0])
        return 1

    def openProject(self):
        open_file = QFileDialog().getOpenFileName(None, '打开工程', '', '*.dms')
        if open_file[0] == "":
            return 0
        openDMSProject(open_file[0])
        self.buildingWgt.updateBuilding()
        return 1

    def initUi(self):
        self.horizonlayout = QVBoxLayout(self)
        self.buildingWgt = DMSBuildingWgt(self)
        self.horizonlayout.addWidget(self.buildingWgt)
        self.centralWidget().setLayout (self.horizonlayout)





