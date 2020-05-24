from datetime import datetime

from sqlalchemy import Table, create_engine, MetaData, select, func, Column, Integer, String, SmallInteger, DateTime

engine = create_engine("sqlite:///C:/Users/JK/Desktop/88.dms")
metadata = MetaData(bind=engine)
#metadata.create_all(engine)

# 开启一个连接
conn = engine.connect()

# 反射表
building = Table("building", metadata, autoload=True, autoload_with=engine)

# 反射库
# metadata.reflect(bind=engine)
# building1 = metadata.tables.get('building')

# table
user = Table("user", metadata,
        Column("id", Integer, nullable=False, primary_key=True, autoincrement=True),
        Column("username", String(20), nullable=False),
        Column("age", Integer, nullable=False),
        Column("sex", SmallInteger, default=1),
        Column("create_time", DateTime, default=datetime.now)
    )

# 插入
def insert():
    ins = building.insert()
    conn.execute(ins, [{"name": "ppp", "age": 20, "sex": 1}, {"name": "mmm", "age": 30, "sex": 0}])
    conn.close()


"""
SELECT project.prj_name AS prj_name, product.prod_name AS prod_name, requirement.req_name AS req_name 
FROM requirement JOIN project ON project.id = requirement.prj_id JOIN product ON product.id = project.prod_id
"""

if __name__ == "__main__":
    insert()
