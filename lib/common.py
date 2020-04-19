def select_func(func_dict):
    for each_key, each_value in func_dict.items():
        print(f'功能编号：{each_key}，对应的功能为：{each_value[0]}')
    while True:
        num_input = input('请输入功能编号：').strip()
        if num_input not in func_dict:
            print('功能编号不存在。')
        else:
            break
    return func_dict[num_input][1]


def auth(user_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            if user_type == 'Admin':
                from core import admin_view as view
            elif user_type == 'Teacher':
                from core import teacher_view as view
            elif user_type == 'Student':
                from core import student_view as view

            if view.user_logged is None:
                print('请登录。')
                view.login()

            return func(*args, **kwargs)

        return wrapper

    return deco


def register():
    while True:
        un_input = input('请输入用户名：').strip()
        if un_input == '':
            print('用户名不能为空。')
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
    return un_input, pw_input


def login():
    while True:
        un_input = input('请输入用户名：').strip()
        if un_input == '':
            print('用户名不能为空。')
        else:
            break
    while True:
        pw_input = input('请输入密码：').strip()
        if pw_input == '':
            print('密码不能为空。')
        else:
            break
    return un_input, pw_input
