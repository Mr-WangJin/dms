import sys
from PyQt5.QtWidgets import QApplication

from ui.utils.dmsCustomTableModel import DMSCustomTableModel
from ui.utils.dmsCustomTableView import DMSCustomTableView

if __name__ == '__main__':

    '''获取系统信息'''
    app = QApplication(sys.argv)

    model = DMSCustomTableModel()

    view =DMSCustomTableView()
    view.setModel(model)
    view.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
