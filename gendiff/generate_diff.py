from gendiff.parse_file import parse_file
from gendiff.format_stylish import format_stylish
from gendiff.format_plain import format_plain
from gendiff.format_json import format_json


def generate_diff(first_file_path, second_file_path, format='stylish'):
    first_file = parse_file(first_file_path)
    second_file = parse_file(second_file_path)
    if format == 'json':
        return format_json(dict_diff(first_file, second_file))
    elif format == 'plain':
        return format_plain(dict_diff(first_file, second_file))
    else:
        return format_stylish(dict_diff(first_file, second_file))


def dict_diff(first_file, second_file):
    result = {}
    keys = sorted(first_file.keys() | second_file.keys())
    for key in keys:
        if key not in first_file:
            result[key] = ('added', second_file[key])
        elif key not in second_file:
            result[key] = ('deleted', first_file[key])
        elif first_file[key] == second_file[key]:
            result[key] = ('not modified', first_file[key])
        elif type(first_file[key]) == dict and type(second_file[key]) == dict:
            result[key] = ('nested modified',
                           dict_diff(first_file[key], second_file[key]))
        else:
            result[key] = ('modified', first_file[key], second_file[key])
    return result
