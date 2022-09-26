# asyncio

## 介绍

- 同步
- 异步

### 同步

同步执行代码时是顺序逐行执行的, 且必须执行完当前行才能执行下一行.

```python
 import time

 print(f"start at {time.strftime('%X')}")
 time.sleep(5)
 time.sleep(3)
 print(f"end at {time.strftime('%X')}")

 start at 10:56:24
 end at 10:56:32
```

以上同步代码, 耗时 8s, sleep 不占用 CPU(I/O 操作执行后也不会占用 CPU), 浪费了 CPU 资源

### 异步

异步执行代码也是顺序执行的, 但是遇到 I/O 阻塞等耗时操作不会等待执行结果, 直接继续执行后续.

异步无法解决庞大计算量的阻塞

```python
 import asyncio
 import time

 async def wait(delay: int, name: str):
     print(f'{name} before')
     await asyncio.sleep(delay)
     print(f'{name} after')

 async def main():
     await asyncio.gather(wait(5, 'first'), wait(3, 'second))

 print(f"start at {time.strftime('%X')}")
 asyncio.run(main())
 print(f"end at {time.strftime('%X')}")

 start at 11:17:44
 first before
 second before
 second after
 first after
 end at 11:17:49

```

使用异步执行时, 只耗时 5s, 两个 wait 函数都执行完成

### 同步代码表示异步

### 协程

### 多线程

多线程就是实现异步的一个方式

## 异步实现

- asyncio.gather
- asyncio.create_task

### asyncio.gather

```python

```

### asyncio.create_task

```python

```

## 异步模块

```python

```

## 同步转异步

- asyncio.to_thread

### asyncio.to_thread

```python

```

### event_loop
