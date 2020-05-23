# encoding: utf-8
# module ui



from PyQt5.QtWidgets import QWidget


class DMSBuildingWgt(QWidget):
    def __init__(self, parent=None):
        super(DMSBuildingWgt, self).__init__(parent)




    def loadBuilding(self, building):
        self.building = building





