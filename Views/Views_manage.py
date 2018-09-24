from Class import School_manage
from Class import Teacher_manage
from Class import Student_manage

print('*********管理系统**********')
def start_view():
    id_choose = input('请选择您的身份：\n1.学校管理员\n2.教师\n3.学生')
    if id_choose == '1':
        School_manage.class_school()
    elif id_choose == '2':
        Teacher_manage.class_teacher()
    elif id_choose == '3':
        Student_manage.class_student()
    else:
        print('您的输入有误，请重新输入')