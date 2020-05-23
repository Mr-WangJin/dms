import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent, QPointF
from PyQt5.QtGui import QMouseEvent, QWheelEvent
from PyQt5.QtWidgets import QApplication, QGraphicsView

from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GScene import GScene
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GSocket import GSocket

DEBUG = True


class NodeEditorView(QGraphicsView):
    zoom = 10
    zoomStep = 1
    zoomRange = range(0, 16, 1)
    zoom_max = 10
    zoom_min = 1
    zoomInFactory = 1.25
    zoomOutFactory = 1 / zoomInFactory
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
        # self.sceneProxy = SceneProxy()
        self.scene=GScene()
        # self.nodeProxy1 = NodeProxy(self.sceneProxy)
        # self.nodeProxy2 = NodeProxy(self.sceneProxy)
        self.operationType = self.NORMAL
        self.newEdgeStatus = None
        self.mouseScenePos = None
        self._initUI()

    def _initUI(self):
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate);
        self.setScene(self.scene)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        #     # elif event.button() == Qt.RightButton:
        #     #     self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    # def mouseReleaseEvent(self, event: QMouseEvent):
    #     # print(event.button(), 'release')
    #     if event.button() == Qt.MidButton:
    #         self.middleMouseButtonRelease(event)
    #     elif event.button() == Qt.LeftButton:
    #         self.leftMouseButtonRelease(event)
    #     else:
    #         super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event: QMouseEvent):
        """When Middle mouse button was pressed"""

        # faking events for enable MMB dragging the scene
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                   Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event: QMouseEvent):
        """When Middle mouse button was released"""
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                Qt.LeftButton, event.buttons() & ~Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.RubberBandDrag)

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
        if isinstance(item, GSocket) and self.operationType == self.NORMAL:
            self.operationType = self.DRAW_NEW_EDGE
            self.edgeInDragging = EdgeProxy(self.sceneProxy)
            self.edgeInDragging.setStartSocketProxy(item.socketProxy)
            self.edgeInDraggingStatus = self.HAD_A_START_SOCKET
            if DEBUG:
                print('a new edge %i had a start socket from %.1f ,%.1f to mouse'
                      % (id(self.edgeInDragging), item.pos().x(), item.pos().y()))
                print('')

        elif isinstance(item, GSocket) and self.operationType == self.DRAW_NEW_EDGE:
            print(id(item.socketProxy.nodeProxy))
            print(id(self.edgeInDragging.startSocketProxy.nodeProxy))
            if id(item.socketProxy.nodeProxy) != id(self.edgeInDragging.startSocketProxy.nodeProxy):
                print('不是同一个node')
                self.edgeInDragging.setEndSocketProxy(item.socketProxy)
                self.edgeInDragging = None
                self.edgeInDraggingStatus = None
                self.operationType = self.NORMAL

        super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        item = self.getItemAtClick(event)
        if isinstance(item, GSocket) and self.START_SOCKET_IS_SELECTED and \
                self.edgeInDragging.startObject.nodeProxy != item.socketProxy.nodeProxy:
            print('2rd socket is click')
            self.edgeInDragging.setEndObject(item)
            self.START_SOCKET_IS_SELECTED = False
            return

        super().mousePressEvent(event)

    # 鼠标移动事件
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.operationType == self.DRAW_NEW_EDGE and self.edgeInDraggingStatus == self.HAD_A_START_SOCKET:
            mouseScenePos = self.mapToScene(event.pos())
            self.edgeInDragging.setEndPosition(mouseScenePos)
            '''触发edge的显示刷新'''
            self.edgeInDragging.gEdge.update()
        super().mouseMoveEvent(event)

    def getItemAtClick(self, event):
        item = self.itemAt(event.pos())
        return item

    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            zoomFactory = self.zoomInFactory
            self.zoom = self.zoom + self.zoomStep
        else:
            zoomFactory = self.zoomOutFactory
            self.zoom = self.zoom - self.zoomStep
        if self.zoom in self.zoomRange:
            self.scale(zoomFactory, zoomFactory)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorView()
    wnd.setGeometry(0, 0, 600, 600)
    wnd.show()

    sys.exit(app.exec_())
