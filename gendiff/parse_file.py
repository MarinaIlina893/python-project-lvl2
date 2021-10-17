import json
import yaml


def parse_file(file_path):
    if file_path.endswith('.yaml') or file_path.endswith('yml'):
        return yaml.load(open(file_path, 'r'), Loader=yaml.Loader)
    if file_path.endswith('.json'):
        return json.load(open(file_path, 'r'))