def format_stylish(diff, indent=2):
    result = ['{']
    for key, value in diff.items():
        if value[0] == 'added':
            add(result, key, value, indent)
        elif value[0] == 'deleted':
            delete(result, key, value, indent)
        elif value[0] == 'not modified':
            add_not_modified(result, key, value, indent)
        elif value[0] == 'modified':
            add_modified(result, key, value, indent)
        else:
            add_nested_modified(result, key, value, indent)
    result.append(' ' * (indent - 2) + '}')
    return '\n'.join(result)


def stylish_value(value):
    dict_ = {True: 'true',
             False: 'false',
             None: 'null'}
    return dict_.get(value, value)


def stylish_dict(dict_, indent):
    result = ['{']
    str_intent = ' ' * indent
    for (key, value) in dict_.items():
        if type(value) == dict:
            result.append(
                f'{str_intent}  {key}: {stylish_dict(value, indent + 4)}')
        else:
            result.append(f'{str_intent}  {key}: {stylish_value(value)}')
    result.append(' ' * (indent - 2) + '}')
    return '\n'.join(result)


def add(result, key, value, indent):
    str_indent = ' ' * indent
    if type(value[1]) == dict:
        result.append(
            f'{str_indent}+ {key}: {stylish_dict(value[1], indent + 4)}')
    else:
        result.append(f'{str_indent}+ {key}: {stylish_value(value[1])}')
    return result


def delete(result, key, value, indent):
    str_indent = ' ' * indent
    if type(value[1]) == dict:
        result.append(
            f'{str_indent}- {key}: {stylish_dict(value[1], indent + 4)}')
    else:
        result.append(f'{str_indent}- {key}: {stylish_value(value[1])}')
    return result


def add_not_modified(result, key, value, indent):
    str_indent = ' ' * indent
    if type(value[1]) == dict:
        result.append(
            f'{str_indent}  {key}: {stylish_dict(value[1], indent + 4)}')
    else:
        result.append(f'{str_indent}  {key}: {stylish_value(value[1])}')
    return result


def add_modified(result, key, value, indent):
    str_indent = ' ' * indent
    if type(value[1]) == dict:
        result.append(
            f'{str_indent}- {key}: {stylish_dict(value[1], indent + 4)}')
    else:
        result.append(f'{str_indent}- {key}: {stylish_value(value[1])}')
    if type(value[2]) == dict:
        result.append(
            f'{str_indent}+ {key}: {stylish_dict(value[2], indent + 4)}')
    else:
        result.append(f'{str_indent}+ {key}: {stylish_value(value[2])}')
    return result


def add_nested_modified(result, key, value, indent):
    str_indent = ' ' * indent
    result.append(
        f'{str_indent}  {key}: {format_stylish(value[1], indent + 4)}')
    return result
