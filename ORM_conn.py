import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#配置连接的数据库
engin=create_engine('mysql+pymysql://root:root@localhost:3306/stsmanage')

#建表需要现有基类
Base=declarative_base()
class Userinfo(Base):
    __tablename__='userinfo'
    id=Column(String(8),primary_key=True)
    name=Column(String(32))
    pw=Column(String(32))

Base.metadata.create_all(engin)

#建立会话session
sessionclass=sessionmaker(bind=engin)
session=sessionclass()

# 增删改查
# 1 add
obj=Userinfo(id='18200135',name='yanhong',pw='123456')
session.add(obj)
session.commit()
# 2 query
query_obj1=session.query(Userinfo).filter_by(name='yanhong')
query_obj2=session.query(Userinfo).filter(Userinfo.name=='yanhong')
print(query_obj1.all())
print(query_obj2.one().name)
#3 改
query_obj2.first().pw='abcd'

session.commit()


#4 delete
session.delete(query_obj2.first())
session.commit()
session.close()




##############################基本查询#########################3
#简单查询
print(session.query(User).all())
print(session.query(User.name, User.fullname).all())
print(session.query(User, User.name).all())

# 带条件查询
print(session.query(User).filter_by(name='user1').all())
print(session.query(User).filter(User.name == "user").all())
print(session.query(User).filter(User.name.like("user%")).all())

# 多条件查询
print(session.query(User).filter(and_(User.name.like("user%"), User.fullname.like("first%"))).all())
print(session.query(User).filter(or_(User.name.like("user%"), User.password != None)).all())

# sql过滤
print(session.query(User).filter("id>:id").params(id=1).all())

# 关联查询
print(session.query(User, Address).filter(User.id == Address.user_id).all())
print(session.query(User).join(User.addresses).all())
print(session.query(User).outerjoin(User.addresses).all())

# 聚合查询
print(session.query(User.name, func.count('*').label("user_count")).group_by(User.name).all())
print(session.query(User.name, func.sum(User.id).label("user_id_sum")).group_by(User.name).all())

# 子查询
stmt = session.query(Address.user_id, func.count('*').label("address_count")).group_by(Address.user_id).subquery()
print(session.query(User, stmt.c.address_count).outerjoin((stmt, User.id == stmt.c.user_id)).order_by(User.id).all())

# exists
print(session.query(User).filter(exists().where(Address.user_id == User.id)))
print(session.query(User).filter(User.addresses.any()))

