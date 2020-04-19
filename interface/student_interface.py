from db import models


def register(username, password):
    stu_obj = models.Student.get_obj(username)
    if stu_obj is not None:
        msg = f'注册失败，学生{username}已存在。'
        return False, msg

    stu_obj = models.Student(username, password)
    stu_obj.save_obj()
    msg = f'学生{username}注册成功。'
    return True, msg


def login(username, password):
    stu_obj = models.Student.get_obj(username)
    if stu_obj is None:
        msg = f'登录失败，学生{username}不存在。'
        return False, msg

    if password != stu_obj.password:
        msg = f'登录失败，学生{username}密码错误。'
        return False, msg
    else:
        msg = f'学生{username}登陆成功。'
        return True, msg


def choose_school(student_name, sch_name):
    stu_obj = models.Student.get_obj(student_name)
    if stu_obj.school_name is not None:
        msg = f'学生{student_name}选择学校{sch_name}失败，已经选择学校{stu_obj.school_name}。'
        return False, msg

    stu_obj.choose_school(sch_name)
    msg = f'学生{student_name}选择学校{sch_name}成功。'
    return True, msg


def get_course_list(student_name):
    stu_obj = models.Student.get_obj(student_name)
    sch_name = stu_obj.school_name
    if sch_name is None:
        msg = f'学生{student_name}尚未选择学校，添加课程失败。'
        return msg, None

    sch_obj = models.School.get_obj(sch_name)
    if len(sch_obj.course_list) == 0:
        msg = f'学生{student_name}的学校{sch_name}尚未开设任何课程，添加课程失败。'
        return msg, None

    return '', sch_obj.course_list


def add_course(student_name, course_name):
    stu_obj = models.Student.get_obj(student_name)
    if course_name in stu_obj.course_list:
        msg = f'课程{course_name}学生{student_name}的课程列表中已存在，添加课程失败。'
        return False, msg

    stu_obj.add_course(course_name)
    msg = f'学生{student_name}添加课程{course_name}成功。'
    return True, msg


def show_score(student_name):
    stu_obj = models.Student.get_obj(student_name)
    if len(stu_obj.score_dict) == 0:
        msg = f'学生{student_name}尚未选择任何课程，查看分数失败。'
        return msg, None

    return '', stu_obj.score_dict
