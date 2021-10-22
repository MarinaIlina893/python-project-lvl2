def format_plain(diff, path=''):
    result = []
    for (key, value) in diff.items():
        if value[0] == 'not modified':
            continue
        elif value[0] == 'modified':
            result.append(
                f'Property \'{path}{key}\' was updated. '
                f'From {stylish_value(value[1])} to {stylish_value(value[2])}')
        elif value[0] == 'deleted':
            result.append(
                f'Property \'{path}{key}\' was removed'
            )
        elif value[0] == 'added':
            result.append(
                f'Property \'{path}{key}\' was added '
                f'with value: {stylish_value(value[1])}')
        else:
            result.append(format_plain(value[1], f'{path}{key}.'))
    return '\n'.join(result)


def stylish_value(value):
    if type(value) == dict:
        return '[complex value]'
    if type(value) == int:
        return value
    dict_ = {True: 'true',
             False: 'false',
             None: 'null'}
    default_value = f'\'{value}\''
    return dict_.get(value, default_value)
