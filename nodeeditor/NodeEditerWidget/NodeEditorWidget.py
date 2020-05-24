import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QApplication, QTableWidget

from bll.dmsContext import dmsProject
from dal.dmsTables import DB_Decorate_Type
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GEdge import GEdge
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GNode import GNode
from nodeeditor.NodeEditerWidget.NodeComponent.GraphicsItems.GScene import GScene
from nodeeditor.NodeEditerWidget.NodeEditorView import NodeEditorView
import re


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
        # taskInfo = {"taskID": "1", "taskName": "任务1"}
        # self.addNode(taskInfo)
        # taskInfo = {"taskID": "2", "taskName": "任务1"}
        # self.addNode(taskInfo)
        pass

    def addNode(self, taskInfo):
        """
        功能设想：通过节点对任务搭接关系进行设置。
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

    def parsePerTaskExpress(self, pre_task: str):
        """
        解析前置任务表达式
        :param pre_task:已校验过为非空对的前置任务表达式
        :return:task_order, task_relation
        """
        task_order = re.match(r'\d+', pre_task, flags=0)
        task_relation = re.match(r'\D+', pre_task, flags=0)
        if task_relation == "":
            task_relation = 'FS'
        else:
            task_relation = str(task_relation).upper()
        if str(task_relation) == 'FS' or str(task_relation) == 'FF' \
                or str(task_relation) == 'SS' or str(task_relation) == 'SF':
            return task_order, task_relation

    def updateTaskNode(self, currentBuildingID):
        """
        当切换页面或者编辑任务或，触发此方法，用于刷新数据。
        1、清空页面
        2、加载数据
        3、绘制节点
        4、绘制连线
        :return:
        """
        # 1、清空页面
        self.scene.clear()
        # 2、加载数据
        decorateTaskList = dmsProject().getTableList(DB_Decorate_Type, filter_str=currentBuildingID)
        # 3、绘制节点
        decorateTask: DB_Decorate_Type
        for decorateTask in decorateTaskList:
            node = GNode(decorateTask)
            node.setPos(decorateTask.node_x, decorateTask.node_y)
            self.nodesDict[node.order] = node
        # 4、绘制连线
        for decorateTask in decorateTaskList:
            currentNodeID = decorateTask.order

            if decorateTask.pre_task != "":
                preTaskOrderList = str(decorateTask.pre_task).split(',')
                for preTask in preTaskOrderList:
                    nodeID, nodeRelation = self.parsePerTaskExpress(preTask)
                    if nodeRelation == "FS":
                        edge = GEdge(startPoint=self.nodesDict.get(nodeID).getFinishSocketPosition,
                                     endPoint=self.nodesDict.get(currentNodeID).getStartSocketPosition())
                        self.edgesDict[nodeID + nodeRelation + str(currentNodeID)] = edge
                    elif nodeRelation == "FF":
                        pass
                    elif nodeRelation == "SS":
                        pass
                    elif nodeRelation == "SF":
                        pass

            else:
                return

    def saveTaskNodeDate2DB(self):
        node: GNode
        for node in self.nodesDict.values():
            value = 'order', node.order, node.scenePos().x(), node.scenePos().y()
            dmsProject().updateRecord(DB_Decorate_Type, value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = NodeEditorWidget()
    wnd.show()
    sys.exit(app.exec_())
