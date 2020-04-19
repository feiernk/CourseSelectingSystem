from lib import common
from core import admin_view, teacher_view, student_view


def admin_func():
    admin_view.admin_func()


def teacher_func():
    teacher_view.teacher_func()


def student_func():
    student_view.student_func()


def run():
    while True:
        func_dict = {
            '0': ('退出', quit),
            '1': ('管理员界面', admin_func),
            '2': ('教师界面', teacher_func),
            '3': ('学生界面', student_func),
        }
        selected_func = common.select_func(func_dict)
        selected_func()
