'''
Helper functions.
'''

import json


def read_db(path):

    with open(path, 'r', encoding='utf-8') as file:
        saved_dict = json.load(file)

    return saved_dict


def save_db(path, dictionary):

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)
