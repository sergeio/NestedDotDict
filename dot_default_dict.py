from collections import defaultdict
from copy import deepcopy


class DotDefaultDict():

    def __init__(self, _type=int):

        def nested_ddict():
            return defaultdict(nested_ddict)

        self._type = _type
        self.ddict = nested_ddict()

    def __setitem__(self, key, value):
        self._set(key, value)

    def _set(self, key, value, subdict=None):

        if subdict is None:
            subdict = self.ddict

        keys = key.split('.', 1)
        if len(keys) == 1:
            subdict[key] = value
        else:
            self._set(keys[1], value, subdict=subdict[keys[0]])

        return self.ddict

    def __str__(self):
        return str(self.ddict)

    def to_dict(self, ddict=None):
        """Returns a deepcopy of `self.ddict`, casted to a dictionary."""

        def _to_dict_helper(ddict):
            copy_ddict = deepcopy(ddict)
            for key, value in copy_ddict.iteritems():
                if type(value) == type(self.ddict):
                    copy_ddict[key] = _to_dict_helper(value)
            return dict(copy_ddict)

        return _to_dict_helper(self.ddict)
