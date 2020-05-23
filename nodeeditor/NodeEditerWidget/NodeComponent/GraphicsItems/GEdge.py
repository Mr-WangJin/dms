import sys

from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QColor, QPainterPath, QBrush
from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsItem, QApplication


class GEdge(QGraphicsPathItem):
    """
    编写原则
    1、可以通过调用父代理类获取的参数，通过调用父代理类获取。尽量不取通过get或set设置。
    2、获取起点终点后，进行类型判断
    """
    pen = QPen(QColor('#ffffff'), 3)
    selected_pen = QPen(QColor('#222222'), 3)

    def __init__(self, edgeProxy):
        super().__init__()
        self.edgeProxy = edgeProxy
        '''socket 用于在绑定了socket情况下的连接线定位'''
        self.startGSocket = None
        self.endGSocket = None
        '''position 用于在没有绑定了socket情况下的鼠标位置定位连接线定位'''
        self.startPosition = None
        self.endPosition = None
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._initUI()

    def _initUI(self):
        self.setZValue(-1)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        print(self.updatePath())
        if self.updatePath():
            QPainter.setPen(self.selected_pen) if self.isSelected() else QPainter.setPen(self.pen)
            QPainter.setBrush(Qt.NoBrush)
            QPainter.drawPath(self.path())
            QPainter.drawLine(self._x2, self._y2, self._x2 - 10, self._y2 - 5)
            QPainter.drawLine(self._x2, self._y2, self._x2 - 10, self._y2 + 5)

    def updatePath(self):
        if self.startGSocket is not None:
            self._x1 = self.startGSocket.scenePos().x()
            self._y1 = self.startGSocket.scenePos().y()
        elif self.startPosition is not None:
            self._x1 = self.startPosition.x()
            self._y1 = self.startPosition.y()
        else:
            return False
        if self.endGSocket is not None:
            self._x2 = self.endGSocket.scenePos().x()
            self._y2 = self.endGSocket.scenePos().y()
        elif self.endPosition is not None:
            self._x2 = self.endPosition.x()
            self._y2 = self.endPosition.y()
        else:
            return False

        print('edge position', self._x1, self._y1, '>>>', self._x2, self._y2)
        if self._x1 < self._x2:
            xc1, yc1 = (self._x1 + self._x2) / 2, self._y1
            xc2, yc2 = (self._x1 + self._x2) / 2, self._y2
        else:
            xc1, yc1 = (self._x1 + 120), self._y1
            xc2, yc2 = (self._x2 - 120), self._y2
        path = QPainterPath(QPointF(self._x1, self._y1))
        path.cubicTo(QPointF(xc1, yc1), QPointF(xc2, yc2), QPointF(self._x2, self._y2))
        self.setPath(path)
        return True
