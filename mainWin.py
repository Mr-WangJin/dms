

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui.mainWin import *


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('装修管理')
        self.ui.actNewProject.triggered.connect(self.newProject)

    def newProject(self):
        openFile = QFileDialog().getSaveFileName(None, '新建工程', '', '*.dms')



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainform = MainWin()
    mainform.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
