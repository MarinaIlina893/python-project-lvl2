from gendiff.parse_file import parse_file


def generate_diff(first_file_path, second_file_path):
    first_file = parse_file(first_file_path)
    second_file = parse_file(second_file_path)
    keys = sorted(first_file.keys() | second_file.keys())
    result = '{\n'
    for key in keys:
        if key not in first_file:
            result = f"{result  }  + {key}: {second_file[key]}" + '\n'
        elif key not in second_file:
            result = f"{result }  - {key}: {first_file[key]}" + '\n'
        elif first_file[key] == second_file[key]:
            result = f'{result}    {key}: {first_file[key]}' + '\n'
        else:
            result = f'{result}  - {key}: {first_file[key]}' + '\n'
            result = f'{result}  + {key}: {second_file[key]}' + '\n'
    return result + '}'
