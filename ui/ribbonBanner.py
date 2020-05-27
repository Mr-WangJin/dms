import sys

from PyQt5.QtCore import QLine, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QWidget, QApplication, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, \
    QFrame


class RibbonButton(QWidget):
    def __init__(self, iconPath, buttonName: str, parent):
        super(RibbonButton, self).__init__(parent=parent)
        self.btn = QPushButton(icon=QIcon(iconPath))
        self.label = QLabel(buttonName)
        self.initUI()

    def initUI(self):
        self.btn.setFixedSize(60, 60)
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(2)
        self.setLayout(vLayout)
        vLayout.addWidget(self.btn)
        vLayout.addWidget(self.label)


class RibbonBanner(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.startTab = QWidget()
        self.startTabLayout = QHBoxLayout()
        self.editTab = QWidget()
        self.editTabLayout = QHBoxLayout()
        self.editTabLayout = QHBoxLayout()
        self.exportTab = QWidget()
        self.exportTabLayout = QHBoxLayout()
        self.hSpacerItem = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        '''开始菜单按钮'''
        self.newProjectBtn = RibbonButton('', '新建工程', self)
        self.openProjectBtn = RibbonButton('', '打开工程', self)
        self.initUI()

    def initUI(self):
        '''组装页签'''
        self.addTab(self.startTab, "开始")
        self.startTab.setLayout(self.startTabLayout)
        self.startTabLayout.setContentsMargins(0, 0, 0, 0)
        self.addTab(self.editTab, "编辑")
        self.editTab.setLayout(self.editTabLayout)
        self.addTab(self.exportTab, "编辑")
        self.exportTab.setLayout(self.exportTabLayout)
        '''开始菜单布局'''
        self.startTabLayout.addWidget(self.newProjectBtn)
        self.startTabLayout.addWidget(self.openProjectBtn)
        self.startTabLayout.addItem(self.hSpacerItem)
        vline = QFrame(self)
        # vline.setGeometry(QRect(190, 210, 3, 61))
        vline.setFrameShape(QFrame.VLine)
        vline.setFrameShadow(QFrame.Sunken)
        vline.setObjectName("line")
        self.startTabLayout.addWidget(vline)
        '''编辑菜单布局'''
        self.addTab(self.editTab, "编辑")
        self.setFixedHeight(120)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMainWindow()
    mainWdg = QWidget()
    vLayout = QVBoxLayout()
    vLayout.setContentsMargins(0, 0, 0, 0)
    vLayout.setSpacing(0)
    vLayout.addWidget(RibbonBanner())
    vLayout.addWidget(QWidget())
    mainWdg.setLayout(vLayout)
    main.setCentralWidget(mainWdg)
    main.showMaximized()
    sys.exit(app.exec_())
