# 数据表定义

from sqlalchemy import Integer, Column, String, true, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


### 单体
class DB_Building(Base):
    __tablename__ = "building"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    order = Column(Integer)

    def __repr__(self):
        return "<User(id= '%s', name='%s')>" % (self.id, self.name)


# ## 户型
# class DB_StructType(Base):
# 	__tablename__ = "struct_type"
#
# 	id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#
# 	building = relationship("building", backref="my_struct_type")

### 单元
class DB_Building_Unit(Base):
    __tablename__ = "building_unit"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    building_id = Column(Integer, ForeignKey("building.id"))
    building = relationship('DB_Building', backref='building_unit_of_building')


### 楼层
class DB_Floor(Base):
    __tablename__ = "floor"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    building_unit_id = Column(Integer, ForeignKey("building_unit.id"))
    building_unit = relationship("DB_Building_Unit", backref="floor_of_building")
    order = Column(Integer)


### 户名
class DB_Struct_Name(Base):
    __tablename__ = "struct_name"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    floor_id = Column(Integer, ForeignKey("floor.id"))
    floor = relationship("DB_Floor", backref="struct_name_floor")


### 装修类型
class DB_Decorate_Type(Base):
    __tablename__ = "decorate_type"

    id = Column(Integer, primary_key=True)
    order = Column(Integer, unique=True)
    name = Column(String(32))
    pre_task = Column(Integer)  # 前置任务
    duration = Column(Integer)  # 工期
    room_belong = Column(String(32))  # 房间归属
    responsible = Column(String(32))  # 责任人
    # node 节点相关参数
    node_color = Column(String(8))  # node 节点颜色
    node_x = Column(Float)  # node 节点位置坐标_x
    node_y = Column(Float)  # node 节点位置坐标_y

    building_id = Column(Integer, ForeignKey("building.id"))
    building = relationship("DB_Building", backref="decorate_type_of_building")


### 单元装修数据
class DB_Unit_Decorate_Data(Base):
    __tablename__ = "unit_decorate_data"

    id = Column(Integer, primary_key=True)
    struct_name_id = Column(Integer, ForeignKey("struct_name.id"))  # 户名
    struct_name = relationship("DB_Struct_Name", backref="decorate_data_of_struct_name")

    building_id = Column(Integer, ForeignKey("building.id"))  # 户名
    building = relationship("DB_Building", backref="decorate_data_of_building")

    data = Column(String)  # json数据


# 数据库版本
class DB_Version(object):
    __tablename__ = "db_version"

    version = Column(Integer)  # 数据库版本
    data_version = Column(Integer)  # 数据版本
