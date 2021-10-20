from gendiff.generate_diff import dict_diff

def test_without_nested():
    file1 = {
                'a': 1,
                'b': 2}

    file2 = {
        'a': 1,
        'b': 3}
    assert dict_diff(file1, file2) == {'a': ('not modified', 1),
                                       'b': ('modified', 2, 3)
                                       }

def test_nested_and_not_nested():
    file1 = {
                'a': {'c': 3},
                'b': 2}

    file2 = {
        'a': 1,
        'b': 2}
    assert dict_diff(file1, file2) == {'a': ('modified', {'c': 3}, 1),
                                       'b': ('not modified', 2)
                                       }

def test_nested_and_nested_similar():
    file1 = {
                'a': {'c': 3},
                'b': 2}

    file2 = {
        'a': {'c': 3},
        'b': 2}
    assert dict_diff(file1, file2) == {'a': ('not modified', {'c': 3}),
                                       'b': ('not modified', 2)
                                       }

def test_nested_and_nested_different():
    file1 = {
                'a': {'c': 4},
                'b': 2}

    file2 = {
        'a': {'c': 3},
        'b': 2}
    assert dict_diff(file1, file2) == {'a': ('nested modified', {'c': ('modified', 4, 3)}),
                                       'b': ('not modified', 2)
                                       }

def test_nested_deleted():
    file1 = {
                'a': {'c': 4},
                'b': 2}

    file2 = {'b': 2}
    assert dict_diff(file1, file2) == {'a': ('deleted', {'c': 4}),
                                       'b': ('not modified', 2)
                                       }
