from gendiff.generate_diff import generate_diff

def test_happy_flow():
    with open('tests/fixtures/generate_diff/result', 'r') as file:
        data = file.read()
    assert generate_diff('tests/fixtures/generate_diff/first.json', 'tests/fixtures/generate_diff/second.json') == data