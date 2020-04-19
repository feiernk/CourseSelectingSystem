from db import models


def login(username, password):
    tch_obj = models.Teacher.get_obj(username)
    if tch_obj is None:
        msg = f'登录失败，教师{username}不存在。'
        return False, msg

    if password != tch_obj.password:
        msg = f'登录失败，教师{username}密码错误。'
        return False, msg
    else:
        msg = f'教师{username}登陆成功。'
        return True, msg


def show_courses(teacher_name):
    tch_obj = models.Teacher.get_obj(teacher_name)
    if len(tch_obj.course_list) == 0:
        msg = f'教师{teacher_name}尚未添加任何课程。'
        return msg, None

    return '', tch_obj.course_list


def add_course(teacher_name, course_name):
    tch_obj = models.Teacher.get_obj(teacher_name)
    if course_name in tch_obj.course_list:
        msg = f'课程{course_name}在教师{teacher_name}的课程列表中已存在，添加课程失败。'
        return False, msg

    tch_obj.add_course(course_name)
    msg = f'教师{teacher_name}添加课程{course_name}成功。'
    return True, msg


def get_course_name_list(teacher_name):
    tch_obj = models.Teacher.get_obj(teacher_name)
    course_name_list = tch_obj.course_list
    if len(course_name_list) == 0:
        msg = f'教师{teacher_name}的课程列表为空。'
        return msg, None
    else:
        return '', course_name_list


def get_student_name_list(teacher_name, course_name):
    crse_obj = models.Course.get_obj(course_name)
    student_name_list = crse_obj.student_list
    if len(student_name_list) == 0:
        msg = f'没有学生选择课程{course_name}。'
        return msg, None
    else:
        return '', student_name_list


def change_score(teacher_name, student_name, course_name, score_int):
    tch_obj = models.Teacher.get_obj(teacher_name)
    tch_obj.change_score(student_name, course_name, score_int)
    msg = f'教师{teacher_name}成绩成功，学生{student_name}的课程{course_name}的成绩为{score_int}。'
    return True, msg
