
# 简化代码控制流

## 分支

- 最小化嵌套
- 正向优先

### 最小化分支

提前退出
优先解决简单问题

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

### 正向优先

正向结果优先

```python
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

分支参数, 左边为变量, 右边为常量

```python
 if num > 5:
    pass

if 5 > num:
    pass

```

## 边界

简化边界问题, 
忽略或合并不关注的内容

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

## 变量的逻辑

### 少创建变量

变量越多负担越重
消除中间变量

```python

note = 'Continue the test when error occurred? (default: Y  N/Y)'
input_raw = input(note) 
input_no_space = input_raw.strip()
input_up = input_no_space.upper()
input_ok = input_up in ('Y', 'N', '')

if input_ok:
    if input_up in ('Y', ''):
        print('continue test when error occurred')
    else:
        print('stop test when error occurred')
else:
    print('input error')


note = 'Continue the test when error occurred? (default: Y  N/Y)'
if input(note).strip().upper() in ('', 'Y'):
    print('continue test when error occurred')
else:
    print('stop test when error occurred')


bmc_cmd = 'systemctl status docker'
cmd_ret = subprocess.Popen(bmc_cmd)
print(bmc_cmd)
print(cmd_ret)

run('systemctl status docker')
```

### 减小变量作用域

减轻变量的追踪难度
声明变量后立即使用

```python

```