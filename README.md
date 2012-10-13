NestedDotDict
=============

A nested dictionary that allows for setting items using dots as a
short-hand for nesting.

## Example:
```python
In [1]: from nested_dot_dict import NestedDotDict

In [2]: nd = NestedDotDict()

In [3]: nd['a.foo'] = 1

In [4]: nd['a.bar'] = 'baz'

In [5]: nd['qux'] = True

In [6]: nd.to_dict()
Out[6]: {'a': {'bar': 'baz', 'foo': 1}, 'qux': True}

In [7]: nd['a.foo']
Out[7]: 1
```
