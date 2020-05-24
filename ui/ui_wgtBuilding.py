# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\projects\dms\ui\ui_wgtBuilding.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wgtBuilding(object):
    def setupUi(self, wgtBuilding):
        wgtBuilding.setObjectName("wgtBuilding")
        wgtBuilding.resize(232, 468)
        self.verticalLayout = QtWidgets.QVBoxLayout(wgtBuilding)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolBtnAdd = QtWidgets.QToolButton(wgtBuilding)
        self.toolBtnAdd.setIconSize(QtCore.QSize(32, 32))
        self.toolBtnAdd.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolBtnAdd.setAutoRaise(True)
        self.toolBtnAdd.setObjectName("toolBtnAdd")
        self.horizontalLayout.addWidget(self.toolBtnAdd)
        self.toolBtnDelete = QtWidgets.QToolButton(wgtBuilding)
        self.toolBtnDelete.setIconSize(QtCore.QSize(32, 32))
        self.toolBtnDelete.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolBtnDelete.setAutoRaise(True)
        self.toolBtnDelete.setObjectName("toolBtnDelete")
        self.horizontalLayout.addWidget(self.toolBtnDelete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(wgtBuilding)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)

        self.retranslateUi(wgtBuilding)
        QtCore.QMetaObject.connectSlotsByName(wgtBuilding)

    def retranslateUi(self, wgtBuilding):
        _translate = QtCore.QCoreApplication.translate
        wgtBuilding.setWindowTitle(_translate("wgtBuilding", "Form"))
        self.toolBtnAdd.setText(_translate("wgtBuilding", "添加"))
        self.toolBtnDelete.setText(_translate("wgtBuilding", "删除"))
