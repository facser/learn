
# 简化代码控制流

## 分支

条件分支

```python
 if num > 5:
    pass

if 5 > num:
    pass


if is_pass:
    # case PASS ...
else:
    # case FAIL ...

if not is_pass:
    # case FAIL ...
else:
    # case PASS ...

if is_fail:
    # case FAIL ...
else:
    # case PASS ...
```


```python
if sut_os_connect():
    if sut_bmc_conect():
        if sut_file_exist():
            # edit file
        else:
            return 'file not exist'
    else:
        return 'bmc connect failed'
else:
    return 'sut os connect failed'


if not sut_os_connect():
    return 'sut os connect failed'

if not sut_bmc_conect():
    return 'bmc connect failed'

if not sut_file_exist():
    return 'file not exist'

# edit file
```



```python

if type(bkm) == int:
    if type(bkms) == list:
        if bkm in bkms:
            return bkms.index(bkm)
        else:
            return f'{bkm} not in {bkms}'
    else:
        return f'{bkms} not a list'
else:
    return f'{bkm} type not int'


try:
    return bkms.index(bkm)
except Exception as e:
    return f'Get {bkm} index error'
```

## 循环

## 变量的逻辑