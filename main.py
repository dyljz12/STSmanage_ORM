from Class import School_manage

print('*********学校管理系统**********')
id_choose=input('请选择您的身份：\n1.学校管理员\n2.教师\n3.学生')
if id_choose=='1':
    School_manage.class_school()
if id_choose=='2':
    pass