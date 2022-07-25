<!--
 * @FilePath: \文档\Learning\python\python-flat-dict.md
 * @Author: facser
 * @Date: 2022-07-25 20:08:15
 * @LastEditTime: 2022-07-25 23:04:32
 * @LastEditors: facser
 * @Description: 
-->

# python flat dictionary

## 引申

字典经常被用来存取数据, 键值对的组合非常便于使用
一个字典可以存储大量数据, 为了便于区分还可以层层分级

对于多层字典存取比较麻烦
插入值的时候需要考虑 key 上层是否存在

能否简化深层字典的存取方式
插入值的时候能否忽略层级问题, 自动生成多级数据

## 字典扁平化

如何简单快捷的进行快速存取深层字典呢?
能否将字典简化成单层结构, 字典内就是 key 和 value

```python
def flat_dict(dic):
    for key, value in dic.items():
        if isinstance(value, dict):
            for k, v in flat_dict(value):
                k = '{key}.{k}'.format(key=key, k=k)
                yield (k, v)
        else:
            yield (key, value)
```

```python
if __name__ == '__main__':
    depth_dict = {'a':{'b': {'c': 0}, 'd':1}, 'c': 1}
    print(dict(flat_dict(depth_dict)))

>>> {'a.b.c': 0, 'a.d': 1, 'c': 1}
```

通过递归循环遍历深层字典, 把多层 key 通过分隔符连接
但是, 这样扁平化无法获取字典类型的 value

```python
def flat_dict(dic):
    for key, value in dic.items():
        yield (key, value)
        if isinstance(value, dict):
            for k, v in flat_dict(value):
                k = '{key}.{k}'.format(key=key, k=k)
                yield (k, v)  
```

```python
if __name__ == '__main__':
    depth_dict = {'a':{'b': {'c': 0}, 'd':1}, 'c': 1}
    print(dict(flat_dict(depth_dict)))

>>> {'a': {'b': {'c': 0}, 'd': 1}, 'a.b': {'c': 0}, 'a.b.c': 0, 'a.d': 1, 'c': 1}
```

增加了字典容量, 但是保存了所有 key 的值

## 字典存取

能将字典扁平化后, 考虑如何存取

```python

```