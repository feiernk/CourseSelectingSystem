from db import db_handler


class Base:
    @classmethod
    def get_obj(cls, obj_name):
        return db_handler.get_obj(cls, obj_name)

    def save_obj(self):
        db_handler.save_obj(self)


class Admin(Base):
    def __init__(self, admin_name, password):
        self.name = admin_name
        self.password = password

    def create_school(self, school_name):
        sch_obj = School(school_name)
        sch_obj.save_obj()

    def create_course(self, school_name, course_name):
        crse_obj = Course(course_name)
        crse_obj.save_obj()
        sch_obj = School.get_obj(school_name)
        sch_obj.course_list.append(course_name)
        sch_obj.save_obj()

    def create_teacher(self, teacher_name, password):
        tch_obj = Teacher(teacher_name, password)
        tch_obj.save_obj()


class School(Base):
    def __init__(self, school_name):
        self.name = school_name
        self.course_list = []


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, password):
        self.name = teacher_name
        self.password = password
        self.course_list = []

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj()

    def change_score(self, student_name, course_name, score_int):
        stu_obj = Student.get_obj(student_name)
        stu_obj.score_dict[course_name] = score_int
        stu_obj.save_obj()


class Student(Base):
    def __init__(self, student_name, password):
        self.name = student_name
        self.password = password
        self.school_name = None
        self.course_list = []
        self.score_dict = {}

    def choose_school(self, school_name):
        self.school_name = school_name
        self.save_obj()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save_obj()
        crse_obj = Course.get_obj(course_name)
        crse_obj.student_list.append(self.name)
        crse_obj.save_obj()
