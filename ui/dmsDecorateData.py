# encoding: utf-8
# 单元下的装修显示数据界面

from PyQt5.QtWidgets import QWidget

from ui.ui_decorateDataWgt import Ui_DecorateDataWgt


class DMSDecorateDataWgt(QWidget):

    def __init__(self, parent=None):
        super(DMSDecorateDataWgt, self).__init__(parent)

        self.ui = Ui_DecorateDataWgt()
        self.ui.setupUi(self)