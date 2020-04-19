from db import db_handler


def get_obj_name_list(cls_name):
    filename_list = db_handler.get_filename_list(cls_name)
    return [each_filename[:-4] for each_filename in filename_list]
