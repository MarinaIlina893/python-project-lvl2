from gendiff.parse_file import parse_file
from gendiff.format import format_stylish


def generate_diff(first_file_path, second_file_path, format='stylish'):
    first_file = parse_file(first_file_path)
    second_file = parse_file(second_file_path)
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
