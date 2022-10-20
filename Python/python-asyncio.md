# asyncio

## 介绍

- 同步
- 异步

### 阻塞

- I/O 阻塞
- 网络 I/O 阻塞

由于 CPU 与内存的交互速度远大于内存与外部设备的交互, 经常会遇到 CPU 需要等待内存与外部设备的交互.
CPU 处理 I/O 操作时需要等待数据从磁盘拷贝到内存, 或将数据从内存拷贝到磁盘. 而 CPU 无法执行任何操作, 称为 I/O 阻塞.
客户端发送请求后, 客户端必须等待接收服务端响应后才能继续后续操作, 称为网络 I/O 阻塞.

### 同步

同步执行代码时是顺序逐行执行的, 且必须执行玩当前行且接受到返回值后才能继续执行下一行.
同步代码有确定的执行顺序, 后面的代码可能会依赖前面代码的执行结果.
同步代码遇到 I/O 或网络请求会产生阻塞

```python
 import time

 print(f"start at {time.strftime('%X')}")
 time.sleep(5)
 time.sleep(3)
 print(f"end at {time.strftime('%X')}")

 start at 10:56:24
 end at 10:56:32
```

### 异步

异步执行遇到异步操作会将其挂起, 继续执行后续代码, 待异步操作完成后, 主线程能收到消息或返回值
异步的执行顺序与代码顺序不一定一致
异步操作之间无数据依赖, 可以独立执行

- 单线程异步
- 多线程异步

单线程异步用于处理非计算密集的如 I/O, 网络请求, 计算密集操作使用单线程异步无效果
多线程异步通过创建新线程完成异步, 计算密集和非计算密集操作都适用, 但线程数量过多会耗费更多资源

## 异步实现

### 多线程异步

- 非计算密集
- 计算密集

```python

def wait(delay: int, name:str):
    print(f'{name} before')
    time.sleep(delay)                            # sleep 操作无需 CPU 计算资源(wait 是非计算密集的)
    print(f'{name} after')

async def main():
    await asyncio.gather(                        # 异步多线程执行 3 个 wait 函数
        asyncio.to_thread(wait, 4, 'first'),
        asyncio.to_thread(wait, 3, 'second'),
        asyncio.to_thread(wait, 4, 'third'),
    )
    
print(f"start at {time.strftime('%X')}")         # 打印开始执行时间
asyncio.run(main())
print(f"end at {time.strftime('%X')}")           # 打印结束执行时间


start at 10:01:36
first before
second before
third before                                     
second after                                     # second 先执行玩, 先出结果
first after
third after
end at 10:01:40                                  # 执行完3个 wait 函数总共耗时 4s
```

上述例子中, python 开了 3 个线程执行 3 个执行 wait 函数, 3个函数执行完后返回结果

```python

def record(num: int, name: str) -> None:
    print(f'{name} begin cal')
    sum = 0
    for i in range(150000000):                   # 计算和, 需要 CPU 计算(计算密集)
        sum += i
    print(f'{name} end cal')

async def main():
    
    await asyncio.gather(                        # 同时开 3 个线程执行 3 record 函数
        asyncio.to_thread(record, 150000000, 'first'),
        asyncio.to_thread(record, 1500000, 'second'),
        asyncio.to_thread(record, 150000000, 'third'),
    )

print(f"start at {time.strftime('%X')}")
asyncio.run(main())
print(f"end at {time.strftime('%X')}")

```

```python
start at 10:13:32
first begin cal
second begin cal
third begin cal
second end cal
first end cal
third end cal
end at 10:13:50                                  # 执行 3 个 record 耗时 18s

start at 09:57:28
first begin cal
first end cal
end at 09:57:34                                  # 执行单个 record 耗时 6s

```

> 注解 由于 GIL 的存在, asyncio.to_thread() 通常只能被用来将 IO 密集型函数变为非阻塞的.
> 对于会释放 GIL 的扩展模块或无此限制的替代性 Python 实现来说, asyncio.to_thread() 也可被用于 CPU 密集型函数.(多进程, 或无 GIL 的 Python)

### 单线程异步

- I/O 阻塞
- 网络通信
- sleep

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
