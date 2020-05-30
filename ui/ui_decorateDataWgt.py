# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programs\Python\dms\ui\ui_decorateDataWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DecorateDataWgt(object):
    def setupUi(self, DecorateDataWgt):
        DecorateDataWgt.setObjectName("DecorateDataWgt")
        DecorateDataWgt.resize(732, 658)
        self.verticalLayout = QtWidgets.QVBoxLayout(DecorateDataWgt)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(DecorateDataWgt)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(DecorateDataWgt)
        QtCore.QMetaObject.connectSlotsByName(DecorateDataWgt)

    def retranslateUi(self, DecorateDataWgt):
        _translate = QtCore.QCoreApplication.translate
        DecorateDataWgt.setWindowTitle(_translate("DecorateDataWgt", "Form"))
