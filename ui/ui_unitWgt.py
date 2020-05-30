# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programs\Python\dms\ui\ui_unitWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UnitWgt(object):
    def setupUi(self, UnitWgt):
        UnitWgt.setObjectName("UnitWgt")
        UnitWgt.resize(710, 548)
        self.verticalLayout = QtWidgets.QVBoxLayout(UnitWgt)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(UnitWgt)
        font = QtGui.QFont()
        font.setFamily("Microsoft Himalaya")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pBtnAddFloor = QtWidgets.QPushButton(UnitWgt)
        self.pBtnAddFloor.setObjectName("pBtnAddFloor")
        self.horizontalLayout_2.addWidget(self.pBtnAddFloor)
        self.pBtnDeleteFloor = QtWidgets.QPushButton(UnitWgt)
        self.pBtnDeleteFloor.setObjectName("pBtnDeleteFloor")
        self.horizontalLayout_2.addWidget(self.pBtnDeleteFloor)
        self.pushButton_3 = QtWidgets.QPushButton(UnitWgt)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(UnitWgt)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(UnitWgt)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pBtnAddUnit = QtWidgets.QPushButton(UnitWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pBtnAddUnit.sizePolicy().hasHeightForWidth())
        self.pBtnAddUnit.setSizePolicy(sizePolicy)
        self.pBtnAddUnit.setMinimumSize(QtCore.QSize(30, 30))
        self.pBtnAddUnit.setMaximumSize(QtCore.QSize(30, 30))
        self.pBtnAddUnit.setSizeIncrement(QtCore.QSize(0, 0))
        self.pBtnAddUnit.setObjectName("pBtnAddUnit")
        self.horizontalLayout.addWidget(self.pBtnAddUnit)
        self.pBtnDleleteUnit = QtWidgets.QPushButton(UnitWgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pBtnDleleteUnit.sizePolicy().hasHeightForWidth())
        self.pBtnDleleteUnit.setSizePolicy(sizePolicy)
        self.pBtnDleleteUnit.setMinimumSize(QtCore.QSize(30, 30))
        self.pBtnDleleteUnit.setMaximumSize(QtCore.QSize(30, 30))
        self.pBtnDleleteUnit.setSizeIncrement(QtCore.QSize(0, 0))
        self.pBtnDleleteUnit.setObjectName("pBtnDleleteUnit")
        self.horizontalLayout.addWidget(self.pBtnDleleteUnit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(UnitWgt)
        QtCore.QMetaObject.connectSlotsByName(UnitWgt)

    def retranslateUi(self, UnitWgt):
        _translate = QtCore.QCoreApplication.translate
        UnitWgt.setWindowTitle(_translate("UnitWgt", "Form"))
        self.label.setText(_translate("UnitWgt", "单元列表"))
        self.pBtnAddFloor.setText(_translate("UnitWgt", "插入楼层"))
        self.pBtnDeleteFloor.setText(_translate("UnitWgt", "删除楼层"))
        self.pushButton_3.setText(_translate("UnitWgt", "插入户型"))
        self.pushButton_5.setText(_translate("UnitWgt", "删除户型"))
        self.pushButton_4.setText(_translate("UnitWgt", "编辑计划"))
        self.pBtnAddUnit.setText(_translate("UnitWgt", "+"))
        self.pBtnDleleteUnit.setText(_translate("UnitWgt", "-"))
