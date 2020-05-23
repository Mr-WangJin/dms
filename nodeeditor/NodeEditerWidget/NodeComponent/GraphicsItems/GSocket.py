import typing

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QBrush, QColor, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem, QWidget, QGraphicsSceneMouseEvent


class GSocket(QGraphicsItem):
    radius = 5
    outside_width = 2
    pen = QPen(QColor('#123456'), outside_width)
    pen_underMouse = QPen(QColor('#123456'), 4)
    brush = QBrush(QColor('#654321'))

    def __init__(self, socketProxy=None, parent=None):
        super().__init__(parent)
        self.socketProxy = socketProxy
        self.initUI()

    def initUI(self):
        pass

    def paint(self, painter: QtGui.QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(self.pen) if not self.isUnderMouse() else painter.setPen(self.pen_underMouse)
        painter.setBrush(self.brush)
        painter.drawEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def boundingRect(self):
        return QRectF(
            -self.radius - self.outside_width,
            -self.radius - self.outside_width,
            2 * (self.radius + self.outside_width),
            2 * (self.radius + self.outside_width)
        )
