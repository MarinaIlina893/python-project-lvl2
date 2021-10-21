from gendiff.format_plain import format_plain


def test_nested_and_not_nested():
    dict_diff = {'a': ('modified', {'c': 3}, 10),
                 'b': ('not modified', 2)
                 }
    with open('tests/fixtures/format_plain/nested_and_not_nested.txt', 'r') as file:
        data = file.read()
    assert format_plain(dict_diff) == data


def test_nested_and_nested_similar():
    dict_diff = {'a': ('not modified', {'c': 3}),
                 'b': ('not modified', 2)
                 }
    assert format_plain(dict_diff) == ''


def test_nested_and_nested_different():
    dict_diff = {'a': ('nested modified', {'c': ('modified', 4, 3)}),
                                       'b': ('not modified', 2)
                                       }
    with open('tests/fixtures/format_plain/nested_and_nested_different.txt',
              'r') as file:
        data = file.read()
    assert format_plain(dict_diff) == data
