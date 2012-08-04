NestedDotDict
=============

A nested dictionary that allows for setting items using dots as a
short-hand for nesting.

## Example:
```python
>>> nd = NestedDotDict()
>>> nd['a.b'] = 2
>>> print nd.to_dict()
{'a': {'b': 2}}
```
