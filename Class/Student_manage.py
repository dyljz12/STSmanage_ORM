import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Views import Views_manage
def class_student():
    # 配置连接的数据库
    engin = create_engine('mysql+pymysql://root:root@localhost:3306/stsmanage')

    # 建表需要现有基类
    Base = declarative_base()

    class Student(Base):
        __tablename__ = 'student'
        name_school = Column(String(8))
        name_student = Column(String(8), primary_key=True)
        name_course = Column(String(8))
        grade = Column(String(8))


    Base.metadata.create_all(engin)
    # 建立会话session
    sessionclass = sessionmaker(bind=engin)
    session = sessionclass()

    print('********学生管理系统********')
    add_name_student = input('请输入您的姓名：')
    def sub_student():
        school_choose = input('请选择操作： \n1.报名课程 \n2.查看课程 \n3.查看成绩 \n4.返回管理系统')
        if school_choose == '1':
            name_school_add = input('请输入要报名的学校')
            course_add = input('请输入要报的课程')
            obj = Student(name_school=name_school_add, name_course=course_add, name_student=add_name_student,
                          grade='未登记')
            session.add(obj)
            session.commit()
            session.close()
            print('报名成功！')
            sub_student()
        elif school_choose == '2':
            obj2 = session.query(Student.name_course).filter(Student.name_student == add_name_student).all()
            for course in obj2:
                print(course[0])
                print('\n')
            session.commit()
            session.close()
            sub_student()
        elif school_choose == '3':
            course_query = session.query(Student.name_course, Student.grade).all()
            for s in course_query:
                print(s[0] + ':' + s[1])
                print('\n')
            session.commit()
            session.close()
            sub_student()

        elif school_choose == '4':
            Views_manage.start_view()
    sub_student()
