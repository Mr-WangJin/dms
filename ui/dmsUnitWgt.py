# encoding: utf-8
# 单元界面
from PyQt5.QtWidgets import QWidget, QTabWidget


class DMSUnitWgt(QTabWidget):

    def __init__(self, parent=None):
        super(DMSUnitWgt, self).__init__(parent)

        # 创建3个选项卡小控件窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")


