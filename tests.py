from dot_default_dict import NestedDotDict


def test_simple():
    dd = NestedDotDict()
    dd['key'] = 0
    assert dd.to_dict() == {'key': 0}


def test_field_creation():
    dd = NestedDotDict()
    dd['s'] = 1
    dd['a.b'] = 2
    dd['a.c'] = 3
    assert dd.to_dict() == {'s': 1, 'a': {'b': 2, 'c': 3}}


def test_more_nesting():
    dd = NestedDotDict()
    dd['a.b.c.d.e.f'] = 1
    assert dd.to_dict() == {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}


def test_longer_key_names():
    dd = NestedDotDict()
    dd['specialization.is.for.insects'] = 1
    assert dd.to_dict() == {'specialization': {'is': {'for': {'insects': 1}}}}


if __name__ == '__main__':
    all_passed = True
    for key, value in locals().items():
        if key.startswith('test_'):
            try:
                value()
                print '.',
            except Exception as e:
                print 'E',
                print e
                all_passed = False

    if all_passed:
        print '\nSuccess!'
    else:
        print '\nFAIL!'
