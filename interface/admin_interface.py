from db import models


def register(username, password):
    admin_obj = models.Admin.get_obj(username)
    if admin_obj is not None:
        msg = f'注册失败，管理员{username}已存在。'
        return False, msg

    admin_obj = models.Admin(username, password)
    admin_obj.save_obj()
    msg = f'管理员{username}注册成功。'
    return True, msg


def login(username, password):
    admin_obj = models.Admin.get_obj(username)
    if admin_obj is None:
        msg = f'登录失败，管理员{username}不存在。'
        return False, msg

    if password != admin_obj.password:
        msg = f'登录失败，管理员{username}密码错误。'
        return False, msg
    else:
        msg = f'管理员{username}登陆成功。'
        return True, msg


def create_school(admin_name, school_name):
    school_obj = models.School.get_obj(school_name)
    if school_obj is not None:
        msg = f'管理员{admin_name}创建学校失败，学校{school_name}已存在。'
        return False, msg

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_school(school_name)
    msg = f'管理员{admin_name}创建学校{school_name}成功。'
    return True, msg


def create_course(admin_name, school_name, course_name):
    school_obj = models.School.get_obj(school_name)
    if course_name in school_obj.course_list:
        msg = f'管理员{admin_name}创建课程失败，学校{school_name}中课程{course_name}已存在。'
        return False, msg

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_course(school_name, course_name)
    msg = f'管理员{admin_name}创建课程{course_name}成功'
    return True, msg


def create_teacher(admin_name, teacher_name, password):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if teacher_obj is not None:
        msg = f'管理员{admin_name}创建教师失败，教师{teacher_name}已存在。'
        return False, msg

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_teacher(teacher_name, password)
    msg = f'管理员{admin_name}创建教师{teacher_name}成功。'
    return True, msg

