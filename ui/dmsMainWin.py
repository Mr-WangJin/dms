
# 主界面

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui.ui_mainWin import Ui_MainWindow


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('装修管理')
        self.ui.actNewProject.triggered.connect(self.newProject)

    def newProject(self):
        openFile = QFileDialog().getSaveFileName(None, '新建工程', '', '*.dms')
        if (openFile == "")
            return ;



