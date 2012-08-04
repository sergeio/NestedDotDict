from dot_default_dict import DotDefaultDict

def test_field_creation():
    dd = DotDefaultDict()
    dd['s'] = 1
    dd['a.b'] = 2
    dd['a.c'] = 3

    assert dd.to_dict() == {'s': 1, 'a': {'b': 2, 'c': 3}}

def test_fail():
    assert False


if __name__ == '__main__':
    all_passed = True
    for key, value in locals().items():
        if key.startswith('test'):
            try:
                value()
                print '.',
            except AssertionError:
                print 'E',
                all_passed = False

    print
    if all_passed:
        print 'Success!'
    else:
        print 'FAIL!'
