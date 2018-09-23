import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def class_school():
    # 配置连接的数据库
    engin = create_engine('mysql+pymysql://root:root@localhost:3306/stsmanage')

    # 建表需要现有基类
    Base = declarative_base()

    class School(Base):
        __tablename__ = 'school'
        name_school = Column(String(8), primary_key=True)
        address = Column(String(32))

    class Teacher(Base):
        __tablename__ = 'teacher'
        name_school = Column(String(8))
        name_teacher = Column(String(8), primary_key=True)

    class Course(Base):
        __tablename__ = 'course'
        name_school = Column(String(8))
        name_teacher = Column(String(8))
        name_course = Column(String(8), primary_key=True)
        price_course = Column(String(8))


    Base.metadata.create_all(engin)
    # 建立会话session
    sessionclass = sessionmaker(bind=engin)
    session = sessionclass()

    print('********学校管理系统********')
    school_choose = input('请选择操作： \n1.增加学校 \n2.删除学校 \n3.学校管理 \n4.返回学校管理系统')
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
        print('目前开设的学校')
        obj4 = session.query(School.name_school).all()
        i = 1
        for sc in obj4:
            number = str(i)
            print('第' + number + '所：' + sc[0])
            i = i + 1
        name_school_delete = input('请输入要删除的学校')
        obj2 = session.query(School).filter(School.name_school == name_school_delete).one()
        session.delete(obj2)
        session.commit()
        session.close()
        print('删除成功！')
        class_school()

    elif school_choose == '3':
        print('目前开设的学校')
        obj4 = session.query(School.name_school).all()
        i=1
        school_list=[]
        for sc in obj4:
            number=str(i)
            print('第'+number+'所：'+sc[0])
            i=i+1
            school_list.append(sc[0])
        school_choose2=input('请选择要管理的学校编码：')
        school_choose_manage=input('请选择管理内容：\n1.招聘老师\n2.解雇老师\n3.开设课程\n4.删除课程\n5.返回学校管理系统')
        school_number=int(school_choose2)-1

        if school_choose_manage=='1':
            imployment_teacher=input('请输入招聘老师的姓名')   #加判断
            session.add(Teacher(name_school=school_list[school_number], name_teacher=imployment_teacher))
            session.commit()
            session.close()
            print('招聘成功')
            class_school()
        elif school_choose_manage=='2':
            pass
        elif school_choose_manage=='3':
            add_course = input('请输入开设的课程')  # 加判断
            add_course_teacher = input('请输入授课老师')
            add_course_price = input('请输入课程价格')
            session.add(Course(name_school=school_list[school_number], name_teacher=add_course_teacher,name_course=add_course,price_course=add_course_price))
            session.commit()
            session.close()
            print('开设课程成功')
            class_school()
        elif school_choose_manage=='4':
            class_school()
        elif school_choose_manage=='5':
            class_school()
        else:
            print('输入有误，请重新输入')
            class_school()



    elif school_choose == '4':
        pass
    else:
        print('输入有误，请重新输入')
        class_school()

