from gendiff.format import format_stylish

def test_nested_and_not_nested():
    dict_diff = {'a': ('modified', {'c': 3}, 10),
                 'b': ('not modified', 2)
                                }
    print(format_stylish(dict_diff))
    with open('tests/fixtures/format/nested_and_not_nested', 'r') as file:
        data = file.read()
    assert format_stylish(dict_diff) == data

def test_nested_and_nested_similar():
    dict_diff = {'a': ('not modified', {'c': 3}),
                 'b': ('not modified', 2)
                 }

    print(format_stylish(dict_diff))
    with open('tests/fixtures/format/nested_and_nested_similar.txt', 'r') as file:
        data = file.read()
    assert format_stylish(dict_diff) == data


def test_nested_and_nested_different():
    dict_diff = {'a': ('nested modified', {'c': ('modified', 4, 3)}),
                                       'b': ('not modified', 2)
                                       }

    print(format_stylish(dict_diff))
    with open('tests/fixtures/format/nested_and_nested_different.txt', 'r') as file:
        data = file.read()
    assert format_stylish(dict_diff) == data