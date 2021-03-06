from gendiff.generate_diff import generate_diff


def test_e2e_only_json():
    with open('tests/fixtures/e2e/result_plain_stylish', 'r') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/e2e/first.json', 'tests/fixtures/e2e/second.json') == data


def test_e2e_only_yaml():
    with open('tests/fixtures/e2e/result_plain_stylish', 'r') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/e2e/first.yaml', 'tests/fixtures/e2e/second.yaml') == data


def test_e2e_json_and_yaml():
    with open('tests/fixtures/e2e/result_plain_stylish', 'r') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/e2e/first.json', 'tests/fixtures/e2e/second.yaml') == data


def test_e2e_nested():
    with open('tests/fixtures/e2e/result_nested_stylish') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/e2e/first_nested.json',
                         'tests/fixtures/e2e/second_nested.json') == data


def test_e2e_nested_plain():
    with open('tests/fixtures/e2e/result_nested_plain.txt',
              'r') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/e2e/first_nested.json',
                         'tests/fixtures/e2e/second_nested.json', 'plain') == data
