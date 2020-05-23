import sys
import threading

from PyQt5.QtCore import QRectF, QLineF
from PyQt5.QtGui import QColor, QBrush, QPainter, QPen
from PyQt5.QtWidgets import QGraphicsScene


class GScene(QGraphicsScene):
    tinny_grid_line_width = 0.5
    bold_grid_line_width = 1.5
    grid_line_color = QColor("#767D8A")
    background_color = QColor('#4C4454')
    gridSize = 20
    rectSize = 64000

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setSceneRect(-self.rectSize / 2, -self.rectSize / 2, self.rectSize, self.rectSize)
        self.setBackgroundBrush(QBrush(self.background_color))

    def drawBackground(self, painter: QPainter, rect: QRectF):
        rect = self.sceneRect()
        super().drawBackground(painter, rect)
        # 绘制纯色背景
        # 绘制网格
        xLines_thin = []
        yLines_thin = []
        xLines_blod = []
        yLines_blod = []
        for i in range(0, self.rectSize, self.gridSize):
            if (i % 100) != 0:
                xLines_thin.append(QLineF(rect.left(), rect.top() + i, rect.right(), rect.top() + i))
                yLines_thin.append(QLineF(rect.left() + i, rect.top(), rect.left() + i, rect.bottom()))
            else:
                xLines_blod.append(QLineF(rect.left(), rect.top() + i, rect.right(), rect.top() + i))
                yLines_blod.append(QLineF(rect.left() + i, rect.top(), rect.left() + i, rect.bottom()))
        painter.setPen(QPen(self.grid_line_color, self.tinny_grid_line_width))
        painter.drawLines(xLines_thin)
        painter.drawLines(yLines_thin)
        painter.setPen(QPen(self.grid_line_color, self.bold_grid_line_width))
        painter.drawLines(xLines_blod)
        painter.drawLines(yLines_blod)
