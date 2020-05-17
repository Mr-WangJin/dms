

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.mainWin import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainform = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainform)

    mainform.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())



