import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def class_teacher():
    # 配置连接的数据库
    engin = create_engine('mysql+pymysql://root:root@localhost:3306/stsmanage')

    # 建表需要现有基类
    Base = declarative_base()

    class Teacher(Base):
        __tablename__ = 'teacher'
        name_school = Column(String(8), primary_key=True)
        name_teacher = Column(String(8))
        name_course = Column(String(8))

    Base.metadata.create_all(engin)
    # 建立会话session
    sessionclass = sessionmaker(bind=engin)
    session = sessionclass()

    print('********教师管理系统********')
    school_choose = input('请选择操作： \n1.增加学校 \n2.删除学校 \n3.查看学校信息 \n4.返回上一级')
    if school_choose == '1':
        name_school_add = input('请输入要增加的学校名称')
        address_school_add = input('请输入要增加的学校地址')
        obj = School(name_school=name_school_add, address=address_school_add)
        session.add(obj)
        session.commit()
        session.close()
        print('增加成功！')
        class_school()
    elif school_choose == '2':
        name_school_delete = input('请输入要删除的学校')
        obj2 = session.query(School).filter(School.name_school == name_school_delete)
        session.delete(obj2)
        session.commit()
        print('删除成功！')
        class_school()
        session.close()
    elif school_choose == '3':
        print('目前建立的学校有：')
        obj4 = session.query(School.name_school).all()
        i=1
        for sc in obj4:
            number=str(i)
            print('第'+number+'所：'+sc[0])
            i=i+1
    elif school_choose == '4':
        pass
    else:
        print('输入有误，请重新输入')
        class_school()

