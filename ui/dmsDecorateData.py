# encoding: utf-8
# 单元下的装修显示数据界面

from PyQt5.QtWidgets import QWidget

from dal.dmsTables import *
from ui.utils import DMSCustomTableView, DMSCustomTableModel
from ui.utils.dmsCustomData import DMSCustomData


class DMSDecorateDataWgt(DMSCustomTableView):

    def __init__(self, parent=None):
        super(DMSDecorateDataWgt, self).__init__(parent)

        self.decorateData = DMSDecorateData()
        self.decorateModel = DMSCustomTableModel()
        self.decorateModel.setCustomData(self.decorateData)
        self.setModel(self.decorateModel)
        # self.ui = Ui_DecorateDataWgt()
        # self.ui.setupUi(self)

    def setCurrentUnit(self):
        pass


class DMSDecorateData(DMSCustomData):

    def __init__(self):
        self.setDisplayTable(DB_Building_Unit)
