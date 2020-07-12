import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent, QPointF
from PyQt5.QtGui import QMouseEvent, QWheelEvent, QPainter
from PyQt5.QtWidgets import QApplication, QGraphicsView

from bll.dmsContext import DMSContext
from dal.dmsTables import DB_Decorate_Type
from ui.nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GNode import GSocket, GNode
from ui.nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GScene import GScene

DEBUG = DMSContext.IS_DEBUG


class NodeEditorView(QGraphicsView):
    ZOOM = 10
    ZOOM_STEP = 1
    ZOOM_RANGE = range(0, 16, 1)
    ZOOM_MAX = 10
    ZOOM_MIN = 1
    ZOOM_IN_FACTORY = 1.2
    ZOOM_OUT_FACTORY = 1 / ZOOM_IN_FACTORY
    START_SOCKET_IS_SELECTED = False
    NORMAL = 0
    DRAW_NEW_EDGE = 1
    MODIFY_EDGE = 2
    # edgeInDraggingStatus
    HAD_NONE_SOCKET = 3
    HAD_A_START_SOCKET = 4
    HAD_A_END_SOCKET = 5
    HAD_ALL_SOCKET = 6

    def __init__(self):
        super().__init__()
        self.edgeInDragging = None
        self.edgeInDraggingStatus = self.HAD_NONE_SOCKET
        self.scene = GScene(self)
        self.operationType = self.NORMAL
        self.newEdgeStatus = None
        self.mouseScenePos = None
        self._initUI()

    def _initUI(self):
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform);
        self.setScene(self.scene)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        '''
        鼠标按下事件
        :param event:
        :return:
        '''
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event: QMouseEvent):
        """When Middle mouse button was pressed"""
        fakeEvent = QMouseEvent(QEvent.MouseButtonRelease,
                                event.localPos(),
                                event.screenPos(),
                                Qt.LeftButton,
                                Qt.NoButton,
                                event.modifiers())
        super().mousePressEvent(fakeEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent = QMouseEvent(QEvent.MouseButtonPress,
                                event.localPos(),
                                event.screenPos(),
                                Qt.LeftButton,
                                event.buttons() | Qt.LeftButton,
                                event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event: QMouseEvent):
        """When Middle mouse button was released"""
        self.setDragMode(QGraphicsView.RubberBandDrag)

        fakeEvent = QMouseEvent(QEvent.MouseButtonRelease,
                                event.localPos(),
                                event.screenPos(),
                                Qt.LeftButton,
                                event.buttons(),
                                event.modifiers())
        super().mouseReleaseEvent(fakeEvent)

    def leftMouseButtonPress(self, event):
        """
        判别操作行为：
        如果没有线在绘制，而且用户点击的是一个socket，
        判定为划线，
            1、设置操作行为为划线
            2、创建一个edge，
               设置edge的起点为用户的点击点
            3、设置edge的终点为鼠标跟随
        如果在划线，且用户点击的是和另一个node的socket
            1、设置edge的终点为socket
            2、清空当前的edge标记对象
            2、设置操作类型为None

        :param event:
        :return:
        """
        """如果点击了一个GSocket,而且这个socket是第一个socket"""
        item = self.getItemAtClick(event)
        print(type(item))
        super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        item = self.getItemAtClick(event)
        if isinstance(item, GSocket) and self.START_SOCKET_IS_SELECTED and \
                self.edgeInDragging.startObject.nodeProxy != item.socketProxy.nodeProxy:
            print('2rd socket is click')
            self.edgeInDragging.setEndObject(item)
            self.START_SOCKET_IS_SELECTED = False
            return

        super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event):
        super().mousePressEvent(event)

    def rightMouseButtonRelase(self, event):
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """鼠标移动事件"""
        if self.operationType == self.DRAW_NEW_EDGE and self.edgeInDraggingStatus == self.HAD_A_START_SOCKET:
            mouseScenePos = self.mapToScene(event.pos())
            self.edgeInDragging.setEndPosition(mouseScenePos)
            '''触发edge的显示刷新'''
            self.edgeInDragging.gEdge.update()
        super().mouseMoveEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        """鼠标滚轮"""
        scrollForward = event.angleDelta().y() > 0
        zoomFactory = self.ZOOM_IN_FACTORY if scrollForward else self.ZOOM_OUT_FACTORY
        self.ZOOM = self.ZOOM + self.ZOOM_STEP if scrollForward else self.ZOOM - self.ZOOM_STEP

        if self.ZOOM in self.ZOOM_RANGE:
            self.scale(zoomFactory, zoomFactory)

    def getItemAtClick(self, event):
        item = self.itemAt(event.pos())
        return item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorView()
    wnd.showMaximized()
    wnd.scene.addItem(GNode(DB_Decorate_Type(name="任务1")))
    wnd.scene.addItem(GNode(DB_Decorate_Type(name="任务2")))
    sys.exit(app.exec_())
