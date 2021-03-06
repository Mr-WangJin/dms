# 业务封装类
from bll.dmsContext import *
from dal.dmsTables import *


def customDeleteRecord(_table, _id):
    _record = dmsDatabase().getRecordById(_table, _id)
    if _record is None:
        return
    dmsDatabase().deleteRecord(_record)


def newBuilding(order: int) -> DB_Building:
    building = DB_Building()
    building.order = dmsDatabase().getCount(DB_Building) + 1
    building.name = building.order.__str__() + '#楼'
    building.order = order
    if dmsDatabase().addRecord(building):
        return building


def updateBuilding(building: DB_Building):
    dmsDatabase().updateRecord(building, {"name": building.name, 'order': building.order})


def deleteBuilding(building: DB_Building):
    dmsDatabase().deleteRecordByID(DB_Building, building)


def newUnit(building: DB_Building) -> DB_Building_Unit:
    if building is None:
        return
    unit = DB_Building_Unit()
    unit.building_id = building.id
    count = dmsDatabase().getTableRecordCount(DB_Building_Unit, "building_id = " + str(building.id))
    unit.name = "测试单元" + str(count)
    dmsDatabase().addRecord(unit)
    return unit


def deleteUnit(business_unit: DB_Building_Unit):
    if business_unit is None:
        return
    dmsDatabase().deleteRecord(business_unit)


def getDecorateType(unit_id) -> List[DB_Decorate_Type]:
    if unit_id:
        return dmsDatabase().getTableList(DB_Decorate_Type, filter_str=unit_id)


class DMSUnitBll(object):
    """单元业务"""

    def __init__(self):
        super(DMSUnitBll, self).__init__()
        pass
