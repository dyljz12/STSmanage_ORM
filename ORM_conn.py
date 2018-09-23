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
# obj=Userinfo(id='18200135',name='yanhong',pw='123456')
# session.add(obj)
session.add(Userinfo(id='18200135',name='yanhong',pw='123456'))
session.commit()
# 2 query
query_obj1=session.query(Userinfo).filter_by(name='yanhong')
query_obj2=session.query(Userinfo).filter(Userinfo.name=='yanhong')
print(query_obj1.all())
print(query_obj2.first())
#3 改
query_obj2.first().pw='abcd'

session.commit()


# #4 delete
# session.delete(query_obj2.first())
# session.commit()
# session.close()

print('success!')