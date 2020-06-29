"""
业务封装类
"""
from typing import List
from bll.dmsContext import *
from dal.dmsTables import *


def customDeleteRecord(_table, _id):
    _record = dmsDatabase().getRecordById(_table, _id)
    if _record is None:
        return
    dmsDatabase().deleteRecord(_record)


# 单体相关业务逻辑
def newBuilding(func) -> DB_Building:
    building = DB_Building()
    building.name = "测试新建单体"
    building.order = dmsDatabase().getMaxOrder(DB_Building) + 1
    return building


def getBuildingList() -> List[DB_Building]:
    return [build for build in dmsDatabase().getTableList(DB_Building)]


def delBuilding(building: DB_Building):
    if building:
        dmsDatabase().deleteRecord(building)


# 单元相关业务逻辑
def newUnit(building: DB_Building) -> DB_Building_Unit:
    if building is None:
        return
    unit = DB_Building_Unit()
    unit.building_id = building.id
    count = dmsDatabase().getTableRecordCount(DB_Building_Unit, "building_id = " + str(building.id))
    unit.name = "测试单元" + str(count)
    dmsDatabase().addRecord(unit)
    return unit


def getUnitList(buildingID) -> List[DB_Building_Unit]:
    if buildingID:
        return [unit for unit in dmsDatabase().getTableList('DB_Building_Unit')]


def deleteUnit(business_unit: DB_Building_Unit):
    if business_unit:
        dmsDatabase().deleteRecord(business_unit)


# 楼层相关业务
def newFloor(unitID: DB_Building_Unit) -> DB_Floor:
    floor = DB_Floor()
    floor.building_unit_id = unitID
    floor.name = ""
    return floor


def defFloor(floor: DB_Floor):
    if floor:
        dmsDatabase().deleteRecord(floor)


def getFloor(unitID):
    if unitID:
        return [floor for floor in dmsDatabase().getTableList('DB_Floor')]


# 计划模板相关业务逻辑
def newDecorateType(buildingID, unitID) -> DB_Decorate_Type:
    decorateType = DB_Decorate_Type()
    decorateType.building_id = buildingID
    decorateType.building_unit_id = unitID
    return decorateType


def deleteDecorateType(decorateType: DB_Decorate_Type):
    if decorateType:
        dmsDatabase().deleteRecord(decorateType)


# 装饰器封装业务逻辑==========================================================================================

def addRecord():
    """
    添加记录装饰器
    :param table: 表对应对类，通过该类获取max_order
    :return:
    """

    def wrapper(*args, **kwargs):
        newRecord = func(*args, **kwargs)
        tableCls = type(newRecord)
        maxOrderNum = dmsDatabase().getMaxOrder(tableCls)
        newRecord.order = maxOrderNum
        dmsDatabase().addRecord(newRecord)
        return newRecord

    return wrapper


def delRecord(func):
    """
    删除记录装饰器
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        record = func(*args, **kwargs)
        if record:
            return dmsDatabase().deleteRecord(record)
        else:
            return

    return wrapper


def updateRecord(func):
    """
    更改记录装饰器
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        record = func(*args, **kwargs)
        dmsDatabase()
        return

    return wrapper


def getRecords(filter=None):
    """
    查询记录装饰器
    :param filter: 查询过滤条件；如果有则按条件查询，如果无则全部查询。
    :return:
    """

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            table: Base = func(*args, **kwargs)
            if filter:
                return [record for record in dmsDatabase().getRecordById(table, filter)]
            else:
                return [record for record in dmsDatabase().getTableList(table)]

        return inner_wrapper

    return wrapper


class DMSUnitBll(object):
    """单元业务"""

    def __init__(self):
        super(DMSUnitBll, self).__init__()
        pass
