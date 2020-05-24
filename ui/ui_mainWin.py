# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\projects\dms\ui\ui_mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        layout = QVBoxLayout()
        self.centralwidget.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actNewProject = QtWidgets.QAction(MainWindow)
        self.actNewProject.setObjectName("actNewProject")
        self.actOpenProject = QtWidgets.QAction(MainWindow)
        self.actOpenProject.setObjectName("actOpenProject")
        self.menuFile.addAction(self.actNewProject)
        self.menuFile.addAction(self.actOpenProject)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setToolTip(_translate("MainWindow", "文件"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.actNewProject.setText(_translate("MainWindow", "新建工程"))
        self.actNewProject.setToolTip(_translate("MainWindow", "新建工程"))
        self.actNewProject.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actOpenProject.setText(_translate("MainWindow", "打开工程"))
        self.actOpenProject.setToolTip(_translate("MainWindow", "打开工程"))
        self.actOpenProject.setShortcut(_translate("MainWindow", "Ctrl+O"))
