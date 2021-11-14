#
# CNOrderedDict
#  This is an implementation to understand how an ordered dictionary is created.
#  This class was built for educational purposes only.
#  Site info was found on : https://www.novixys.com/blog/python-class-methods-ordered-dictionary/
#  November 2021 (C)
#

class CNOrderedDict:
    """ CNOrderedDict is an Ordered dictionary. """
    class _Iter:
        def __init__(self, arr):
            self.a = arr
            self.c = 0
        def __next__(self):
            i = self.c
            if i >= len(self.a):
                raise StopIteration
            self.c += 1
            return self.a[i].k

    class _Item:
        """
        Internal Class used by the dictionary
        """
        def __init__(self, key, value):
            self.k = key
            self.v = value

    def __init__(self):
        self.d = {}
        self.a = []

    def __iter__(self):
        return CNOrderedDict._Iter(self.a)

    def _find(self, key):
        """Not sure why we do a sequential search here and just do dictionary lookup"""
        for i in self.a:
            if i.k == key: return i
        return None

    def __setitem__(self, key, value):
        if key in self.d:
            item = self._find(key)
            item.v = value
        else:
            self.d[key] = value
            self.a.append(CNOrderedDict._Item(key, value))

    def __getitem__(self, key):
        """This can return an invalid index and should use get"""
        return self.d[key]

    def __delitem__(self, key):
        del self.d[key]
        a = []
        for i in self.a:
            if i.k != key: a.append(i)
        self.a = a

    def __contains__(self, key):
        return dict.__contains__(self.d, key)

    def __iter__(self):
        return CNOrderedDict._Iter(self.a)

    def __len__(self):
        return len(self.d)

    def __str__(self):
        s = ''
        for i in self.a:
            if s: s += ', '
            if isinstance(i.v, (int, float)):
                v = str(i.v)
            else:
                v = "'" + str(i.v) + "'"
            s += "'" + str(i.k) + "'" + ': ' + v
        return '{' + s + '}'
