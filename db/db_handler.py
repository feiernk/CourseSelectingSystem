import os
import pickle

from conf import settings


def get_obj(cls, obj_name):
    cls_folder_path = os.path.join(settings.DB_FOLDER_PATH, cls.__name__)
    if not os.path.isdir(cls_folder_path):
        return None

    obj_filepath = os.path.join(cls_folder_path, f'{obj_name}.pkl')
    if not os.path.isfile(obj_filepath):
        return None
    else:
        with open(obj_filepath, mode='rb') as f:
            obj = pickle.load(f)
        return obj


def save_obj(obj):
    cls_folder_path = os.path.join(settings.DB_FOLDER_PATH, obj.__class__.__name__)
    if not os.path.isdir(cls_folder_path):
        os.mkdir(cls_folder_path)

    obj_filepath = os.path.join(cls_folder_path, f'{obj.name}.pkl')
    with open(obj_filepath, mode='wb') as f:
        pickle.dump(obj, f)


def get_filename_list(cls_name):
    cls_folder_path = os.path.join(settings.DB_FOLDER_PATH, cls_name)
    if not os.path.isdir(cls_folder_path):
        return None

    return os.listdir(cls_folder_path)
