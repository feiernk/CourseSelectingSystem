from lib import common
from interface import admin_interface, common_interface

user_logged = None


def register():
    while True:
        un_input, pw_input = common.register()
        flg, msg = admin_interface.register(un_input, pw_input)
        if not flg:
            print(msg)
        else:
            print(msg)
            break


def login():
    while True:
        un_input, pw_input = common.login()
        flg, msg = admin_interface.login(un_input, pw_input)
        if not flg:
            print(msg)
        else:
            global user_logged
            user_logged = un_input
            print(msg)
            break


@common.auth('Admin')
def create_school():
    while True:
        sch_name_input = input('请输入学校名：').strip()
        if sch_name_input == '':
            print('学校名不能为空。')
        else:
            break
    flg, msg = admin_interface.create_school(user_logged, sch_name_input)
    print(msg)


@common.auth('Admin')
def create_course():
    sch_name_list = common_interface.get_obj_name_list('School')
    if not sch_name_list:
        print(f'创建课程失败，学校不存在。')
        return

    for i, each_sch_name in enumerate(sch_name_list):
        print(f'编号：{i}，学校名：{each_sch_name}')
    while True:
        num_input = input('请输入学校编号：').strip()
        if num_input == '':
            print('输入不能为空。')
            continue

        num_int = int(num_input)
        if num_int not in range(len(sch_name_list)):
            print('编号不存在。')
        else:
            sch_name = sch_name_list[num_int]
            break
    while True:
        crse_input = input('请输入课程名称：').strip()
        if crse_input == '':
            print('课程名不能为空。')
        else:
            break
    flg, msg = admin_interface.create_course(user_logged, sch_name, crse_input)
    print(msg)


@common.auth('Admin')
def create_teacher():
    while True:
        tch_input = input('请输入教师名：').strip()
        if tch_input == '':
            print('教师名不能为空。')
        else:
            break
    while True:
        pw_input = input('请输入密码：').strip()
        if pw_input == '':
            print('密码不能为空。')
            continue
        pw_re_input = input('请再次输入密码：').strip()
        if pw_input != pw_re_input:
            print('两次输入的密码不一致。')
        else:
            break
    flg, msg = admin_interface.create_teacher(user_logged, tch_input, pw_input)
    print(msg)


def admin_func():
    while True:
        func_dict = {
            '0': ('退出', quit),
            '1': ('注册', register),
            '2': ('登录', login),
            '3': ('创建学校', create_school),
            '4': ('创建课程', create_course),
            '5': ('创建老师', create_teacher),
        }
        selected_func = common.select_func(func_dict)
        selected_func()
