

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from bll.dmsProject import *
from ui.ui_mainWin import Ui_MainWindow


class DMSMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(DMSMainWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('装修管理')
        self.ui.actNewProject.triggered.connect(self.newProject)
        self.ui.actOpenProject.triggered.connect(self.openProject)

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
        return 1




