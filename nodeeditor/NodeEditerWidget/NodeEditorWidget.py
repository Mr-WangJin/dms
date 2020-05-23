import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QApplication

from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GEdge import GEdge
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GNode import GNode
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GScene import GScene
from nodeeditor.NodeEditerWidget.NodeEditorView import NodeEditorView


class NodeEditorWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.view = NodeEditorView()
        self.scene = GScene()
        self.nodesDict: [str, GNode] = {}
        self.edgesDict: [str, GEdge] = {}
        self.__initUI__()
        self.addDemoNode()

    def __initUI__(self):
        self.view.setScene(self.scene)
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        layout = QHBoxLayout()
        layout.addWidget(self.view)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def addDemoNode(self):
        taskInfo = {"taskID": "1", "taskName": "任务1"}
        self.addNode(taskInfo)
        taskInfo = {"taskID": "2", "taskName": "任务1"}
        self.addNode(taskInfo)

    def addNode(self, taskInfo):
        """

        :param taskInfo:
        :return:
        1、封装信息
        2、按ID添加Node到字典
        3、绘制Node图形
        """

        gNode = GNode(taskInfo)
        print(taskInfo["taskID"])
        if self.nodesDict.get(taskInfo["taskID"]) is None:
            self.nodesDict[taskInfo["taskID"]] = gNode
            self.scene.addItem(gNode)
            return True
        else:
            return False

    def freshGraphics(self):
        """
        用于切换单体时，刷新Node布局
        :return:
        """
        pass

    def freshNodeStatus(self):
        """
        用于更新数据时，刷新Node数据和状态
        :return:
        """
        pass

    def loadData(self):
        pass

    def setAllNodesPos(self):
        pass

    def parse2Graph(self, tasksInfo):
        """
        用于从数据库读取计划模版，解析网络关系，构建连接线。
        !!!  sequenceID要在包内唯一
        1、构件图结构
            { 任务序号1，[前置任务1,前置任务2] ,
              任务序号2，[前置任务1,前置任务2] ,
              任务序号3，[前置任务1,前置任务2] }
        2、计算节点布局
        3、添加连接线
        :param tasksInfo:
        :return:
        """
        graph: {str, []} = dict
        for taskID, taskSequenceID, taskName, aheadTask, duration in tasksInfo:
            graph['taskSequenceID'] = []

        for taskID, taskSequenceID, taskName, aheadTask, duration in tasksInfo:
            graph[taskSequenceID].append()

    def parseSSFS(self, aheadTask: str):
        if len(aheadTask) != 0: return
        aheadTaskList = aheadTask.split(',')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorWidget()
    wnd.show()
    sys.exit(app.exec_())
