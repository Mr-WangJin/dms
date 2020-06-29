# 数据表定义
from datetime import datetime

from sqlalchemy import Integer, Column, String, true, ForeignKey, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DB_Building(Base):
    """
    单体
    """
    __tablename__ = "building"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    order = Column(Integer)

    __mapper_args__ = {"order_by": order}

    def __repr__(self):
        return "<User(id= '%s', name='%s')>" % (self.id, self.name)


class DB_Building_Unit(Base):
    """
    单元
    """
    __tablename__ = "building_unit"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    order = Column(Integer)

    building_id = Column(Integer, ForeignKey("building.id"))
    building = relationship('DB_Building', backref='building_unit_of_building')

    __mapper_args__ = {"order_by": order}


class DB_Floor(Base):
    """
    楼层
    """
    __tablename__ = "floor"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    building_unit_id = Column(Integer, ForeignKey("building_unit.id"))
    building_unit = relationship("DB_Building_Unit", backref="floor_of_building")
    order = Column(Integer)


class DB_Struct_Name(Base):
    """
    户名
    """
    __tablename__ = "struct_name"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    floor_id = Column(Integer, ForeignKey("floor.id"))
    floor = relationship("DB_Floor", backref="struct_name_floor")


class DB_Decorate_Type(Base):
    """
    计划模板

    """
    __tablename__ = "decorate_type"

    id = Column(Integer, primary_key=True, comment='主键')
    order = Column(Integer, unique=True, comment='序号')
    name = Column(String(32), comment='任务名称')
    pre_task = Column(String(32), comment='前置任务')
    duration = Column(Integer, comment='工期')
    room_belong = Column(String(32), comment='房间')
    responsible = Column(String(32), comment='责任人')
    # node 节点相关参数
    node_color = Column(String(8), comment='颜色')  # node 节点颜色
    node_x = Column(Float, comment='X')  # node 节点位置坐标_x
    node_y = Column(Float, comment='Y')  # node 节点位置坐标_y

    # building_id = Column(Integer, ForeignKey("building.id"))  # 单体外键
    # building = relationship("DB_Building", backref="decorate_type_of_building")
    #
    # building_unit_id = Column(Integer, ForeignKey("building_unit.id"))  # 单元外键
    # building_unit = relationship("DB_Building_Unit", backref="floor_of_building")


class DB_Unit_Decorate_Data(Base):
    """
    单元装修数据
    """
    __tablename__ = "unit_decorate_data"

    id = Column(Integer, primary_key=True)
    update_data = Column(Date)  # 登记时间
    building_id = Column(Integer, ForeignKey("building.id"))  # 户名
    struct_name_id = Column(Integer, ForeignKey("struct_name.id"))  # 户名
    struct_name = relationship("DB_Struct_Name", backref="decorate_data_of_struct_name")
    building = relationship("DB_Building", backref="decorate_data_of_building")
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    data = Column(String)  # json数据


class DB_Version(object):
    """数据库版本"""

    __tablename__ = "db_version"

    version = Column(Integer)  # 数据库版本
    data_version = Column(Integer)  # 数据版本
