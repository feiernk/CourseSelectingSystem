from lib import common
from interface import student_interface, common_interface

user_logged = None


def register():
    while True:
        un_input, pw_input = common.register()
        flg, msg = student_interface.register(un_input, pw_input)
        if not flg:
            print(msg)
        else:
            print(msg)
            break


def login():
    while True:
        un_input, pw_input = common.login()
        flg, msg = student_interface.login(un_input, pw_input)
        if not flg:
            print(msg)
        else:
            global user_logged
            user_logged = un_input
            print(msg)
            break


@common.auth('Student')
def choose_school():
    school_name_list = common_interface.get_obj_name_list('School')
    if not school_name_list:
        print(f'选择学校失败，学校不存在。')
        return
    for i, each_school_name in enumerate(school_name_list):
        print(f'编号：{i}，学校名：{each_school_name}')
    while True:
        num_input = input('请输入学校编号：').strip()
        if num_input == '':
            print('输入不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(school_name_list)):
            print('编号不存在。')
        else:
            school_name = school_name_list[num_int]
            break
    flg, msg = student_interface.choose_school(user_logged, school_name)
    print(msg)


@common.auth('Student')
def choose_course():
    msg, course_name_list = student_interface.get_course_list(user_logged)
    if course_name_list is None:
        print(msg)
        return
    for i, each_course_name in enumerate(course_name_list):
        print(f'编号：{i}，学校名：{each_course_name}')
    while True:
        num_input = input('请输入课程编号：').strip()
        if num_input == '':
            print('输入不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(course_name_list)):
            print('编号不存在。')
        else:
            course_name = course_name_list[num_int]
            break
    flg, msg = student_interface.add_course(user_logged, course_name)
    return msg


@common.auth('Student')
def show_score():
    msg, course_dict = student_interface.show_score(user_logged)
    if course_dict is None:
        print(msg)
    else:
        for each_key, each_value in course_dict.items():
            print(f'课程：{each_key}，分数：{each_value}。')


def student_func():
    while True:
        func_dict = {
            '0': ('退出', quit),
            '1': ('注册', register),
            '2': ('登录', login),
            '3': ('选择学校', choose_school),
            '4': ('选择课程', choose_course),
            '5': ('查看分数', show_score),
        }
        selected_func = common.select_func(func_dict)
        selected_func()
