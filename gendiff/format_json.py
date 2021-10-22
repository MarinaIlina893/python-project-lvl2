import json


def format_json(diff):
    result = {}
    for (key, value) in diff.items():
        if value[0] == 'added':
            result[key] = f'+ {value[1]}'
        elif value[0] == 'deleted':
            result[key] = f'- {value[1]}'
        elif value[0] == 'not modified':
            result[key] = f'= {value[1]}'
        elif value[0] == 'modified':
            result[key] = f'- {value[1]} + {value[2]}'
        else:
            result[key] = format_json(value[1])
    return json.dumps(result, indent=4)
