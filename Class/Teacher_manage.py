import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Views import Views_manage
def class_teacher():
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

    print('********教师管理系统********')
    teacher_name = input('请输入您的名字')
    def sub_teacher():
        school_choose = input('请选择操作： \n1.查看学生信息 \n2.登记学生成绩  \n3.返回管理系统')
        if school_choose == '1':
            obj1 = session.query(Course, Student).join(Student, Course.name_course == Student.name_course).filter(Course.name_teacher == teacher_name).all()
            # # obj_temp=Course()
            # # obj_temp=obj1[0]
            # print(obj_temp.name_course)
            print('姓名:' + obj1[0][1].name_student + ',所修课程' + obj1[0][0].name_course)
            session.commit()
            session.close()
            sub_teacher()
        elif school_choose == '2':
            student_name = input('学生名字:')
            student_grade = input('成绩:')
            obj2 = session.query(Student).filter(Student.name_student == student_name)
            obj2.one().grade = student_grade
            session.commit()
            session.close()
            sub_teacher()
        elif school_choose == '3':
            Views_manage.start_view()
        else:
            print('输入有误，请重新输入')
            sub_teacher()

    sub_teacher()
