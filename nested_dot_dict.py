from collections import defaultdict
from copy import deepcopy


class NestedDotDict(defaultdict):
    """This dict lets you easily create and query a highly-nested structure."""

    def __init__(self, _type=int):

        def nested_ddict():
            return defaultdict(nested_ddict)

        self._type = _type
        defaultdict.__init__(self, nested_ddict)

    def __getitem__(self, key):
        def _get(key, subdict):
            keys = key.split('.', 1)
            if len(keys) == 1:
                return defaultdict.__getitem__(subdict, key)
            return _get(keys[1], subdict[keys[0]])

        return _get(key, self)

    def __setitem__(self, key, value):
        def _set(key, value, subdict):
            keys = key.split('.', 1)
            if len(keys) == 1:
                defaultdict.__setitem__(subdict, key, value)
            else:
                _set(keys[1], value, subdict[keys[0]])

        _set(key, value, self)

    def to_dict(self):
        """Returns a copy of `self`, recursively casted to a dict."""

        def _to_dict_helper(ddict):
            copy_ddict = deepcopy(ddict)
            for key, value in copy_ddict.iteritems():
                if type(value) == defaultdict:
                    copy_ddict[key] = _to_dict_helper(value)
            return dict(copy_ddict)

        return _to_dict_helper(self)
