# encoding: utf-8
# 装修类型界面
import sys
import uuid
from typing import List

from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QTableWidget, QApplication, QAbstractItemView, QAction, QToolBar, QVBoxLayout, QPushButton, \
    QSizePolicy, QSpacerItem, QTableWidgetItem
from qtconsole.qt import QtGui

from bll.dmsContext import dmsDatabase
from dal.dmsTables import DB_Decorate_Type
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GNode import GNode


class DMSDecorateTypeWgt(QDialog):
    DEBUG = True
    tableWdg = None
    # 数据列位置
    TASK_ID = 0
    TASK_ORDER = 1
    TASK_NAME = 2
    TASK_DURATION = 3
    TASK_PRE = 4
    TASK_ROOM_BELONG = 5
    TASK_RESPONSIBLE = 6
    TASK_NODE_X = 7
    TASK_NODE_Y = 8
    TASK_NODE_COLOR = 9
    # 表头
    HEADER_NAME = ["id", '序号', '任务名称', '工期', '前置任务', '房间', '责任人', "x", "y", "颜色"]

    TOOL_BAR_HEIGHT = 30
    TABLE_HEADER_HEIGHT = 30

    def __init__(self, parent=None):
        super(DMSDecorateTypeWgt, self).__init__(parent)
        self.tableWdg = QTableWidget(0, len(DMSDecorateTypeWgt.HEADER_NAME))
        self.toolBar = QToolBar('toolBar', self)
        self.actInsertTask = QAction(text="插入")
        self.actDelTask = QAction(text="删除")
        self.toolBar.addAction(self.actInsertTask)
        self.toolBar.addAction(self.actDelTask)
        self.commitBtn = QPushButton("确定")
        self.cancelBtn = QPushButton("取消")
        self.initUI()
        self.initSignal()
        pass

    def initSignal(self):
        self.actInsertTask.triggered.connect(self.addDecorateType)
        self.actDelTask.triggered.connect(self.delDecorateType)

    def initUI(self):
        # 布局
        self.setWindowTitle("编辑计划模板")
        self.setWindowModality(Qt.WindowModal)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        layout.addWidget(self.toolBar)
        layout.addWidget(self.tableWdg)
        # bottomBar

        bottomBar = QHBoxLayout()
        bottomBar.setSpacing(20)
        bottomBar.setContentsMargins(10, 10, 16, 16)
        spacerItem = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottomBar.addItem(spacerItem)
        bottomBar.addWidget(self.commitBtn)
        bottomBar.addWidget(self.cancelBtn)
        self.commitBtn.setFixedSize(80, 40)
        self.cancelBtn.setFixedSize(80, 40)
        layout.addLayout(bottomBar)
        self.resize(800, 600)
        # toolBar
        self.toolBar.setFixedHeight(DMSDecorateTypeWgt.TOOL_BAR_HEIGHT)
        # table
        '''隐藏不必要的列'''
        if self.DEBUG is False:
            self.tableWdg.hideColumn(DMSDecorateTypeWgt.TASK_ID)
            self.tableWdg.hideColumn(DMSDecorateTypeWgt.TASK_NODE_X)
            self.tableWdg.hideColumn(DMSDecorateTypeWgt.TASK_NODE_Y)
            self.tableWdg.hideColumn(DMSDecorateTypeWgt.TASK_NODE_COLOR)
        '''设置表头表列'''
        self.tableWdg.horizontalHeader().setFixedHeight(DMSDecorateTypeWgt.TABLE_HEADER_HEIGHT)
        self.tableWdg.setHorizontalHeaderLabels(DMSDecorateTypeWgt.HEADER_NAME)
        self.tableWdg.verticalHeader().setVisible(False)
        '''设置选择和编辑行为'''
        self.tableWdg.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.AnyKeyPressed)
        # Todo
        # self.tableWdg.setSelectionBehavior(QAbstractItemView.sel)

    def updateDecorateType(self, currentBuilding):
        self.tableWdg.clear()
        task: DB_Decorate_Type
        decorateTaskList: List[DB_Decorate_Type] = dmsDatabase().getTableList(table=DB_Decorate_Type, filter_str=currentBuilding)
        rowNumber = 0
        for task in decorateTaskList:
            taskID = QTableWidgetItem(task.id)
            taskOrder = QTableWidgetItem(task.order)
            taskName = QTableWidgetItem(task.name)
            taskPre = QTableWidgetItem(task.pre_task)
            taskDuration = QTableWidgetItem(task.duration)

            self.tableWdg.setItem(rowNumber, 1, taskName)

            itemOrder = QTableWidgetItem(task.order)

    def getCurrentItem(self):
        return self.tableWdg.currentItem()

    def addDecorateType(self):
        itemList = self.tableWdg.selectedItems()
        rowNum = self.tableWdg.rowCount() if len(itemList) == 0 else itemList[0].row()
        self.tableWdg.insertRow(rowNum)
        self.tableWdg.setItem(rowNum, self.TASK_ID, QTableWidgetItem(str(uuid.uuid1())))
        self.tableWdg.setItem(rowNum, self.TASK_NODE_X, QTableWidgetItem("0"))
        self.tableWdg.setItem(rowNum, self.TASK_NODE_Y, QTableWidgetItem("0"))
        self.tableWdg.setItem(rowNum, self.TASK_NODE_COLOR, QTableWidgetItem(str(GNode.brush.color().rgba())))

    def delDecorateType(self):
        itemList = self.tableWdg.selectedItems()
        if len(itemList) == 0:
            return
        else:
            taskID = self.tableWdg.itemAt(itemList[0].row(), DMSDecorateTypeWgt.TASK_ID).data(Qt.UserRole)
            self.tableWdg.removeRow(itemList[0].row())

    def saveDecorateTypeDate2DB(self):
        pass

    def checkDateVisable(self):
        # 数据校验
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DMSDecorateTypeWgt()
    win.show()
    sys.exit(app.exec_())
