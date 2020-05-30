# 业务封装类
from bll.dmsContext import *
from dal.dmsTables import *


def newBuilding() -> DB_Building:
    building = DB_Building()
    building.name = "测试新建单体"
    building.order = dmsDatabase().getMaxOrder(DB_Building)+1
    return building


def newUnit(building: DB_Building) -> DB_Building_Unit:
    unit = DB_Building_Unit()
    unit.building_id = building.id
    count = dmsDatabase().getTableRecordCount(DB_Building_Unit, "building_id = " + str(building.id))
    unit.name = "测试单元" + str(count)
    dmsDatabase().addRecord(unit)
    return unit


class DMSUnitBll(object):
    """单元业务"""

    def __init__(self):
        super(DMSUnitBll, self).__init__()
        pass
