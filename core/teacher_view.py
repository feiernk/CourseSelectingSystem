from lib import common
from interface import teacher_interface, common_interface

user_logged = None


def login():
    while True:
        un_input, pw_input = common.login()
        flg, msg = teacher_interface.login(un_input, pw_input)
        if not flg:
            print(msg)
        else:
            global user_logged
            user_logged = un_input
            print(msg)
            break


@common.auth('Teacher')
def show_courses():
    msg, course_name_list = teacher_interface.show_courses(user_logged)
    if course_name_list is None:
        print(msg)
    else:
        print(f'教师{user_logged}教授的课程为{", ".join(course_name_list)}')


@common.auth('Teacher')
def add_course():
    course_name_list = common_interface.get_obj_name_list('Course')
    if not course_name_list:
        print('管理员尚未添加课程，无法选择。')
    else:
        for i, each_course_name in enumerate(course_name_list):
            print(f'课程编号：{i}，课程名称：{each_course_name}')
        while True:
            num_input = input('请输入课程编号：').strip()
            if num_input == '':
                print('课程编号不能为空。')
                continue

            num_int = int(num_input)
            if num_int not in range(len(course_name_list)):
                print('课程编号不存在。')
            else:
                course_name = course_name_list[num_int]
                break
    flg, msg = teacher_interface.add_course(user_logged, course_name)
    print(msg)


@common.auth('Teacher')
def show_student():
    msg, course_name_list = teacher_interface.get_course_name_list(user_logged)
    if course_name_list is None:
        print(msg)
        return

    for i, each_course_name in enumerate(course_name_list):
        print(f'课程编号：{i}，课程名称：{each_course_name}')
    while True:
        num_input = input('请输入课程编号：').strip()
        if num_input == '':
            print('课程编号不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(course_name_list)):
            print('课程编号不存在。')
        else:
            course_name = course_name_list[num_int]
            break
    msg, student_name_list = teacher_interface.get_student_name_list(user_logged, course_name)
    if student_name_list is None:
        print(msg)
    else:
        print(f'课程{course_name}中的学生：{", ".join(student_name_list)}')


@common.auth('Teacher')
def change_score():
    msg, course_name_list = teacher_interface.get_course_name_list(user_logged)
    if course_name_list is None:
        print(msg)
        return

    for i, each_course_name in enumerate(course_name_list):
        print(f'课程编号：{i}，课程名称：{each_course_name}')
    while True:
        num_input = input('请输入课程编号：').strip()
        if num_input == '':
            print('课程编号不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(course_name_list)):
            print('课程编号不存在。')
        else:
            course_name = course_name_list[num_int]
            break
    msg, student_name_list = teacher_interface.get_student_name_list(user_logged, course_name)
    if student_name_list is None:
        print(msg)
        return

    for i, each_student_name in enumerate(student_name_list):
        print(f'学生编号：{i}，学生名字：{each_student_name}')
    while True:
        num_input = input('请输入学生编号：').strip()
        if num_input == '':
            print('学生编号不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(student_name_list)):
            print('学生编号不存在。')
        else:
            student_name = student_name_list[num_int]
            break

    while True:
        score_input = input('请输入成绩：').strip()
        if score_input == '':
            print('成绩不能为空。')
        elif not score_input.isdigit():
            print('只接受数字。')
        else:
            break

    score_int = int(score_input)
    flg, msg = teacher_interface.change_score(user_logged, student_name, course_name, score_int)
    print(msg)


def teacher_func():
    while True:
        func_dict = {
            '0': ('退出', quit),
            '1': ('登录', login),
            '2': ('查看课程', show_courses),
            '3': ('添加课程', add_course),
            '4': ('查看课程的学生', show_student),
            '5': ('修改分数', change_score),
        }
        selected_func = common.select_func(func_dict)
        selected_func()
