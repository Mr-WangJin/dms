
# 数据表定义

from sqlalchemy import Integer, Column, String, true, ForeignKey
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

### 户型
# class DB_StructType(Base):
# 	__tablename__ = "struct_type"

# 	id = Column(Integer, primary_key=True)
#     name = Column(String(32))

# 	building = relationship("building", backref="my_struct_type")

### 单元
class DB_Building_Unit(Base):
    __tablename__ = "building_unit"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    building_id = relationship("building", backref="my_building")


### 楼层
class DB_Floor(Base):
    __tablename__ = "floor"

    id = Column(Integer, primary_key=true)
    name = Column(String(32))
    building_unit_id = relationship("building_unit", backref="my_building_unit")
    order = Column(Integer)

### 户名
class DB_Struct_Name(Base):
    __tablename__ = "struct_name"

    id = Column(Integer, primary_key=true)
    name = Column(String(32))
    floor_id = relationship("floor", backref="my_floor")


### 装修类型
class DB_Decorate_Type(Base):
    __tablename__ = "struct_name"

    id = Column(Integer, primary_key=true)
    order = Column(Integer)
    pre_task = Column(Integer) #前置任务
    duration = Column(Integer) #工期
    room_belong = Column(String(32)) #房间归属
    responsible = Column(String(32)) #责任人

    building_id = Column(Integer, ForeignKey("building.id")) #户名
    building = relationship("building", backref="my_building")

### 单元装修数据
class DB_Unit_Decorate_Data(Base):
    __tablename__ = "unit_decorate_data"

    id = Column(Integer, primary_key=true)
    struct_name_id = Column(Integer, ForeignKey("struct_name.id")) #户名
    struct_name = relationship("struct_name", backref="my_struct_name")

    building_id = Column(Integer, ForeignKey("building.id")) #户名
    building = relationship("building", backref="my_building")

    data = Column(String) # json数据



class DB_Version(object):
    __tablename__ = "db_version"

    version = Column(Integer)		#数据库版本
    data_version = Column(Integer)	#数据版本




