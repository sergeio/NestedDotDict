import sys

from nested_dot_dict import NestedDotDict


def test_simple():
    nd = NestedDotDict()
    nd['key'] = 0
    assert nd.to_dict() == {'key': 0}


def test_field_creation():
    nd = NestedDotDict()
    nd['s'] = 1
    nd['a.b'] = 2
    nd['a.c'] = 3
    assert nd.to_dict() == {'s': 1, 'a': {'b': 2, 'c': 3}}


def test_more_nesting():
    nd = NestedDotDict()
    nd['a.b.c.d.e.f'] = 1
    assert nd.to_dict() == {'a': {'b': {'c': {'d': {'e': {'f': 1}}}}}}


def test_longer_key_names():
    nd = NestedDotDict()
    nd['specialization.is.for.insects'] = 1
    assert nd.to_dict() == {'specialization': {'is': {'for': {'insects': 1}}}}


def test_getting():
    nd = NestedDotDict()
    nd['a.b.c'] = 1
    nd['a.b.d'] = 2
    assert nd['a.b.c'] == 1
    assert nd['a.b.d'] == 2


if __name__ == '__main__':
    for key, value in locals().items():
        if key.startswith('test_'):
            try:
                value()
                print '.',
            except Exception as e:
                print 'E\n', e
                sys.exit(1)

    print '\nSuccess!'
