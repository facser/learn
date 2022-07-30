
from json import dumps
from collections import defaultdict


class Flat(dict):
    
    def __init__(self, depth):
        dict.__init__(self, depth)
        self.dict_flat = {}
        self.dict_depth = depth

    def flat_dict(self, dic):
        for key, value in dic.items():
            yield (key, value)
            if isinstance(value, dict):
                for k, v in self.flat_dict(value):
                    k = '{key}.{k}'.format(key=key, k=k)
                    yield (k, v)

    def update_depth_dict(self, key, value):

        key_list = key.split('.')
        dic = self

        for k in key_list[:-1]:
            dic.setdefault(k, {})
            dic = dic[k]

        dic.update({key_list[-1]: value})

    def __setitem__(self, key, value):
        self.dict_flat[key] = value
        self.update_depth_dict(key, value)

    def __getitem__(self, key):
        try:
            return self.dict_flat[key]
        except KeyError:
            self.dict_flat.update(dict(self.flat_dict(self)))
            return self.dict_flat[key]

    def __str__(self):
        return dumps(self, indent=4)


dic = Flat({})

# dic['a'] = 3
dic['a.b.c.e'] = 2

dic['a.b.d'] = 3
dic['a.b.d'] = 5

dic['c'] = 3

# dic['b.a'] = 4
# dic.update({'b': 3})

# print(dic.get('a'))
print(dic)




