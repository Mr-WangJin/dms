import platform

from PyQt5 import QtCore
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QFont, QColor, QBrush, QPen, QPainter, QPainterPath
from PyQt5.QtWidgets import QStyle, QGraphicsItem, QGraphicsTextItem, QGraphicsLineItem, QStyleOptionGraphicsItem

from dal.dmsTables import DB_Decorate_Type

import typing

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QBrush, QColor, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class GNode(QGraphicsItem):
    '''节点尺寸'''
    node_width = 300
    node_height = 120
    cell_width = 100
    cell_height = 30
    '''坐标位置'''
    # ---------------------
    # |          1        |
    # ---------------------
    # |   2   |  3  |  4  |
    # ---------------------
    # |   5   |  6  |  7  |
    # ---------------------
    # |          8        |
    # ---------------------
    padding = 4
    position_1 = padding, padding
    position_2 = padding, padding + cell_height
    position_3 = padding + cell_width, padding + cell_height
    position_4 = padding + cell_width * 2, padding + cell_height
    position_5 = padding, padding + cell_height * 2
    position_6 = padding + cell_width, padding + cell_height * 2
    position_7 = padding + cell_width * 2, padding + cell_height * 2
    position_8 = padding, padding + cell_height * 3
    # 文本样式
    title_font_win = QFont('微软雅黑', 12, 100)
    title_font_mac = QFont('PingFang Sc', 12, 100)
    title_color = QColor('#767D8A')
    title_width = node_width
    # 图形样式
    pen_width = 2
    pen = QPen(QColor("#ffffff"), 0)
    selected_pen = QPen(QColor("#E37C4C"), pen_width)
    brush = QBrush(QColor("#C7EEE7"))
    radius = 6

    def __init__(self, decorateTask: DB_Decorate_Type, parent=None):
        """
        1、本图例为节点图例，内有多个子图例，该自图例在实例化时，必须要注意传入self，否则子图例不知道父图例是谁，
        就无法和父图例一同展示到scene上。
        2、之前由于没有实现父类到boundingRect方法，导致拖拽和选中无效
        3、
        :param nodeProxy:
        """
        super().__init__(parent=parent)
        self.gID = decorateTask.id
        self.order = decorateTask.order
        self.gTaskName = QGraphicsTextItem(decorateTask.name, self)
        self.gAmount = QGraphicsTextItem('总空间数量', self)
        self.gTeamCount = QGraphicsTextItem('班组数量', self)
        self.gIsFlowable = QGraphicsTextItem('是否可流水', self)
        self.gStartTime = QGraphicsTextItem('开始时间', self)
        self.gDuration = QGraphicsTextItem(decorateTask.duration, self)
        self.gFinishTime = QGraphicsTextItem('结束时间', self)
        self.gFinishCount = QGraphicsTextItem('已完空间数量', self)
        self.gBackgroundColor = QColor("#C7EEE7")
        self.setPos(0, 0)

        # socket
        self.gLeftSocket = GSocket(parent=self)
        self.gRightSocket = GSocket(parent=self)
        # 绘制图形
        self._initUI()
        self._initInterAction()

    def _initUI(self):
        self.gLeftSocket.setZValue(10)
        self.gRightSocket.setZValue(10)
        self._initTextItemStyle()
        self._initTextItemPosition()
        self._initSplitLine()
        self._initSocektPositon()

    def _initInterAction(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def _initTextItemStyle(self):
        textItems = [
            self.gTaskName,
            self.gAmount,
            self.gTeamCount,
            self.gIsFlowable,
            self.gStartTime,
            self.gDuration,
            self.gFinishTime,
            self.gFinishCount
        ]
        for item in textItems:
            self._setDefaultTextStyle(item)

    def _setDefaultTextStyle(self, textItem: QGraphicsTextItem):
        textItem.setDefaultTextColor(self.title_color)
        textItem.setFont(self.title_font_win) if platform.system() == 'Windows' else self.gTaskName.setFont(self.title_font_mac)

    def _initTextItemPosition(self):
        self.gTaskName.setPos(GNode.position_1[0], GNode.position_1[1])
        self.gAmount.setPos(GNode.position_2[0], GNode.position_2[1])
        self.gTeamCount.setPos(GNode.position_3[0], GNode.position_3[1])
        self.gIsFlowable.setPos(GNode.position_4[0], GNode.position_4[1])
        self.gStartTime.setPos(GNode.position_5[0], GNode.position_5[1])
        self.gDuration.setPos(GNode.position_6[0], GNode.position_6[1])
        self.gFinishTime.setPos(GNode.position_7[0], GNode.position_7[1])
        self.gFinishCount.setPos(GNode.position_8[0], GNode.position_8[1])

    def _initSocektPositon(self):
        self.gLeftSocket.setPos(0, GNode.node_height / 2)
        self.gRightSocket.setPos(GNode.node_width, GNode.node_height / 2)

    def _initSplitLine(self):
        line1 = QGraphicsLineItem(0 + GNode.pen_width, GNode.cell_height, GNode.node_width - GNode.pen_width, GNode.cell_height, self)
        line2 = QGraphicsLineItem(0 + GNode.pen_width, GNode.cell_height * 2, GNode.node_width - GNode.pen_width, GNode.cell_height * 2, self)
        line3 = QGraphicsLineItem(0 + GNode.pen_width, GNode.cell_height * 3, GNode.node_width - GNode.pen_width, GNode.cell_height * 3, self)
        # 竖分割线
        line4 = QGraphicsLineItem(GNode.cell_width, GNode.cell_height, GNode.cell_width, GNode.cell_height * 3, self)
        line5 = QGraphicsLineItem(GNode.cell_width * 2, GNode.cell_height, GNode.cell_width * 2, GNode.cell_height * 3, self)

    def boundingRect(self) -> QtCore.QRectF:
        return QRectF(
            0,
            0,
            self.radius + self.node_width + self.radius,
            self.radius + self.node_height + self.radius
        ).normalized()

    def paint(self, painter: QPainter, option, widget=None) -> None:
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.node_width, self.node_height, self.radius, self.radius)
        painter.setPen(self.selected_pen) if self.isSelected() else painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPath(path)
        option.state = QStyle.State_None

    def getStartSocketPosition(self, ):
        # print(self.mapToScene(self.gStartSocket.pos().toPoint()))
        return self.mapToScene(self.gLeftSocket.pos().toPoint())

    def getFinishSocketPosition(self, ):
        # print(self.mapToScene(self.gFinishSocket.pos().toPoint()))
        return self.mapToScene(self.gRightSocket.pos().toPoint())

    def getNodeData(self):
        point = self.mapToScene(self.pos().toPoint())
        return self.gID, self.gTaskName, self.x(), point.y()


class GSocket(QGraphicsItem):
    '''size'''
    radius = 5
    outside_width = 2
    '''color'''
    outline_color = '#ffffff'
    background_color = '#ffffff'

    pen = QPen(QColor(outline_color), outside_width)
    pen_underMouse = QPen(QColor(outline_color), outside_width)
    brush = QBrush(QColor(background_color))

    def __init__(self, socketProxy=None, parent=None):
        super().__init__(parent)
        self.socketProxy = socketProxy
        self.initUI()

    def initUI(self):
        pass

    def paint(self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(self.pen_underMouse) if self.isUnderMouse() else painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def boundingRect(self):
        return QRectF(
            -self.radius - self.outside_width,
            -self.radius - self.outside_width,
            2 * (self.radius + self.outside_width),
            2 * (self.radius + self.outside_width)
        )
