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
 print(f"close at {time.strftime('%X')}")

 start at 10:56:24
 close at 10:56:32
```

### 异步

异步执行遇到异步操作会将其挂起并返回, 继续执行后续代码, 待异步操作完成后, 主线程能收到消息或返回值
异步的执行顺序与代码顺序不一定一致
异步操作之间无数据依赖, 可以独立执行

```javascript

const wait = async (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    setTimeout(() => {
        console.log(`${name} ${delay} ${(new Date()).toString()}`);
    }, delay*1000);
}

const main = () => {
    wait("first ", 4);
    wait("second", 2);
    wait("third ", 6);
    console.log("Over")
}
  
main()


first  4 Tue Nov 22 2022 15:58:19 GMT+0800 (China Standard Time)
second 2 Tue Nov 22 2022 15:58:19 GMT+0800 (China Standard Time)
third  6 Tue Nov 22 2022 15:58:19 GMT+0800 (China Standard Time)
Over
second 2 Tue Nov 22 2022 15:58:21 GMT+0800 (China Standard Time)
first  4 Tue Nov 22 2022 15:58:23 GMT+0800 (China Standard Time)
third  6 Tue Nov 22 2022 15:58:25 GMT+0800 (China Standard Time)
```

单线程异步用于处理非计算密集的如 I/O, 网络请求, 计算密集操作使用单线程异步无效果
多线程异步通过创建新线程完成异步, 计算密集和非计算密集操作都适用, 但线程数量过多会耗费更多资源

## 异步实现

### 多线程异步

主线程跳过异步操作, 新开线程执行跳过的操作, 使主线程运行达到异步效果

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

var wg sync.WaitGroup

func Delay(name string, delay int) {
    defer wg.Done()
    fmt.Println(name, delay, time.Now())
    time.Sleep(time.Duration(delay) * time.Second)
    fmt.Println(name, delay, time.Now())
}

func main() {
    names := [...]string{"first", "second", "third"}
    delays := [...]int{4, 3, 5}
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go Delay(names[i], delays[i])
    }

    // time.Sleep(3 * time.Second)
    fmt.Println("Over")
    wg.Wait()                                              // 等待所有协程执行完成                                      
}

Over
third    5 2022-11-21 10:26:36.9768235 +0800 CST m=+0.000138501
second   3 2022-11-21 10:26:36.9770264 +0800 CST m=+0.000341101
first    4 2022-11-21 10:26:36.977027  +0800 CST m=+0.000341901
second   3 2022-11-21 10:26:39.9793892 +0800 CST m=+3.002704301
first    4 2022-11-21 10:26:40.9779395 +0800 CST m=+4.001255201
third    5 2022-11-21 10:26:41.9782989 +0800 CST m=+5.001614301

Over
third    5 2022-11-21 10:27:17.1999131 +0800 CST m=+0.000108201
first    4 2022-11-21 10:27:17.2000231 +0800 CST m=+0.000218101
second   3 2022-11-21 10:27:17.2000865 +0800 CST m=+0.000281801
second   3 2022-11-21 10:27:20.2025237 +0800 CST m=+3.002719501
first    4 2022-11-21 10:27:21.200926  +0800 CST m=+4.001121601
third    5 2022-11-21 10:27:22.201361  +0800 CST m=+5.001556601


second   2 2022-11-22 16:18:03.4051558 +0800 CST m=+0.000249701
third    6 2022-11-22 16:18:03.405007 +0800 CST m=+0.000100801
first    4 2022-11-22 16:18:03.4050635 +0800 CST m=+0.000157601
second   2 2022-11-22 16:18:05.4066026 +0800 CST m=+2.001696701
Over
first    4 2022-11-22 16:18:07.4066345 +0800 CST m=+4.001729001
third    6 2022-11-22 16:18:09.4070635 +0800 CST m=+6.002157901
```

从上面代码和结果可知, main 和新开的 3 个 Delay 有 4 个线程, 执行顺序由协程耗时决定

### 单线程异步

```python
import asyncio

async def wait(name:str, delay:int) -> None:               # 定义 wait 延时函数模拟 IO 阻塞, 打印开始和结束时间 
    print(f"{name:<8} {delay} {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(f"{name:<8} {delay} {time.strftime('%X')}")

async def main() -> None:
    await asyncio.gather(                                  # 异步执行 3 个延时函数
        asyncio.create_task(wait('first',  4)),
        asyncio.create_task(wait('second', 2)),
        asyncio.create_task(wait('third',  6)),
    )

if __name__ == 'main':
    asyncio.run(main())


first    4 16:11:52
second   2 16:11:52
third    6 16:11:52
second   2 16:11:54
first    4 16:11:56
third    6 16:11:58
```

### CPU

```python

import asyncio
import time

def record(name: str, end: int, ) -> None:
    print(f"{name:<8} {end} {time.strftime('%X')}")
    sum = 0
    for i in range(end):
        sum += i
    print(f"{name:<8} {end} {time.strftime('%X')}")

def wait(name:str, delay:int) -> None:
    print(f"{name:<8} {delay} {time.strftime('%X')}")
    time.sleep(delay)
    print(f"{name:<8} {delay} {time.strftime('%X')}")
    
async def main():
    await asyncio.gather(
        asyncio.to_thread(wait, 'first',  4),
        asyncio.to_thread(wait, 'second', 2),
        asyncio.to_thread(wait, 'third',  6),
    )    

    await asyncio.gather(
        asyncio.to_thread(record, 'first',  60000000),
        asyncio.to_thread(record, 'second', 10000000),
        asyncio.to_thread(record, 'third',  30000000),
    )
    
if __name__ == 'main':
    asyncio.run(main())


first    4 16:43:40
second   2 16:43:40
third    6 16:43:40
second   2 16:43:42
first    4 16:43:44
third    6 16:43:46
first    40000000 16:43:46
second   20000000 16:43:46
third    60000000 16:43:46
second   20000000 16:43:51
first    40000000 16:43:53
third    60000000 16:43:55

```

```python
first    40000000 16:45:06
second   20000000 16:45:06
third    60000000 16:45:06
second   20000000 16:45:11
first    40000000 16:45:14
third    60000000 16:45:16                                 # 3 个协程花费 10 s

first    40000000 16:45:38
first    40000000 16:45:41                                 # 单个协程花费 3 s

second   20000000 16:46:13
second   20000000 16:46:15                                 # 单个协程花费 2 s

third    60000000 16:46:32
third    60000000 16:46:36                                 # 单个协程花费 4 s
```

> 注解 由于 GIL 的存在, asyncio.to_thread() 通常只能被用来将 IO 密集型函数变为非阻塞的.
> 对于会释放 GIL 的扩展模块或无此限制的替代性 Python 实现来说, asyncio.to_thread() 也可被用于 CPU 密集型函数.(多进程, 或无 GIL 的 Python)

### 单线程异步

- I/O 阻塞
- 网络通信
- sleep

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

```Go
package main

import (
    "fmt"
    "sync"
    "time"
)

var wg sync.WaitGroup

func Sum(name string, end int) {
    defer wg.Done()
    fmt.Println(name, end, time.Now())
    sum := 0
    for i := 0; i <= end; i++ {
        sum += i
    }
    fmt.Println(name, end, time.Now())
}

func main() {
    names := [...]string{"first", "second", "third"}
    delays := [...]int{15000000000, 1000000000, 13000000000}
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go Sum(names[i], delays[i])
    }
    fmt.Println("Over")
    wg.Wait()
}

third    20000000000 2022-11-22 10:51:36.4803571 +0800 CST m=+0.000173601
second   10000000000 2022-11-22 10:51:36.4804665 +0800 CST m=+0.000283101
first    15000000000 2022-11-22 10:51:36.4804039 +0800 CST m=+0.000220401
second   10000000000 2022-11-22 10:51:41.7277742 +0800 CST m=+5.247590701
first    15000000000 2022-11-22 10:51:43.8958834 +0800 CST m=+7.415699901
third    20000000000 2022-11-22 10:51:45.9174494 +0800 CST m=+9.437265801

third    20000000000 2022-11-22 10:51:00.7876033 +0800 CST m=+0.000169201
third    20000000000 2022-11-22 10:51:08.1227567 +0800 CST m=+7.335322701
```

```python
first    40000000 15:22:03                       # python 多进程
second   20000000 15:22:03
third    60000000 15:22:03
second   20000000 15:22:04
first    40000000 15:22:06
third    60000000 15:22:07

first    40000000 15:23:55
first    40000000 15:23:58

second   20000000 15:25:07
second   20000000 15:25:08

third    60000000 15:24:32
third    60000000 15:24:36
```

```python
first    40000000 15:27:18                       # python 多线程
second   20000000 15:27:18
third    60000000 15:27:18
second   20000000 15:27:24
first    40000000 15:27:28
third    60000000 15:27:29


first    40000000 15:27:40
first    40000000 15:27:43

second   20000000 15:27:58
second   20000000 15:27:59

third    60000000 15:28:13
third    60000000 15:28:17
```

```javascript
const wait = async (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    setTimeout(() => {
        console.log(`${name} ${delay} ${(new Date()).toString()}`);
    }, delay*1000);
}

const main = () => {
    wait("first ", 4);
    wait("second", 2);
    wait("third ", 6);
}
  
main()

first  4 Tue Nov 22 2022 11:04:58 GMT+0800 (China Standard Time)
second 2 Tue Nov 22 2022 11:04:58 GMT+0800 (China Standard Time)
third  6 Tue Nov 22 2022 11:04:58 GMT+0800 (China Standard Time)
second 2 Tue Nov 22 2022 11:05:00 GMT+0800 (China Standard Time)
first  4 Tue Nov 22 2022 11:05:02 GMT+0800 (China Standard Time)
third  6 Tue Nov 22 2022 11:05:04 GMT+0800 (China Standard Time)
```

```javascript

const record = (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    return new Promise((resolve) => {
        let sum = 0;
        for (let i=0; i<delay; i++) {
            sum += i;
        };
        console.log(`${name} ${delay} ${(new Date()).toString()}`);
    });
};


const main = () => {
    record("first ", 1500000000);
    record("second", 1000000000);
    record("third ", 2000000000);
}
  
main()


first  1500000000 Tue Nov 22 2022 11:01:47 GMT+0800 (China Standard Time)
first  1500000000 Tue Nov 22 2022 11:01:50 GMT+0800 (China Standard Time)
second 1000000000 Tue Nov 22 2022 11:01:50 GMT+0800 (China Standard Time)
second 1000000000 Tue Nov 22 2022 11:01:51 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:01:51 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:01:54 GMT+0800 (China Standard Time)

third  2000000000 Tue Nov 22 2022 11:02:24 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:02:27 GMT+0800 (China Standard Time)
```

```javascript

const record = (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    return new Promise((resolve) => {
        let sum = 0;
        for (let i=0; i<delay; i++) {
            sum += i;
        };
        console.log(`${name} ${delay} ${(new Date()).toString()}`);
    });
};


const main = () => {
    record("first ", 1500000000);
    record("second", 1000000000);
    record("third ", 2000000000);
}
  
main()


first  1500000000 Tue Nov 22 2022 11:01:47 GMT+0800 (China Standard Time)
first  1500000000 Tue Nov 22 2022 11:01:50 GMT+0800 (China Standard Time)
second 1000000000 Tue Nov 22 2022 11:01:50 GMT+0800 (China Standard Time)
second 1000000000 Tue Nov 22 2022 11:01:51 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:01:51 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:01:54 GMT+0800 (China Standard Time)

third  2000000000 Tue Nov 22 2022 11:02:24 GMT+0800 (China Standard Time)
third  2000000000 Tue Nov 22 2022 11:02:27 GMT+0800 (China Standard Time)
```

```javascript

const readSync = (name, file) => {
    console.log(`${name} ${(new Date()).toString()}`);
    require("fs").readFileSync(file);
    console.log(`${name} ${(new Date()).toString()}`);
}

const readAsync = (name, file) => {
    console.log(`${name} ${(new Date()).toString()}`);
    require('fs').readFile(file, function (err, data) {
        console.log(`${name} ${(new Date()).toString()}`);
    });
}

const main = () => {
    readSync("first ", "read/one_line_1.log")
    readSync("second", "read/one_line_2.log")
    readSync("third ", "read/one_line_3.log")

    readAsync("first ", "read/one_line_1.log")
    readAsync("second", "read/one_line_2.log")
    readAsync("third ", "read/one_line_3.log")
}

main()

first  Wed Nov 23 2022 11:06:10 GMT+0800 (China Standard Time)
first  Wed Nov 23 2022 11:06:13 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 11:06:13 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 11:06:18 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 11:06:18 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 11:06:24 GMT+0800 (China Standard Time)


first  Wed Nov 23 2022 11:22:25 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 11:22:25 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 11:22:25 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 11:22:33 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 11:22:41 GMT+0800 (China Standard Time)
first  Wed Nov 23 2022 11:22:42 GMT+0800 (China Standard Time)
```

JS的单线程是指一个浏览器进程中只有一个JS的执行线程，同一时刻内只会有一段代码在执行（你可以使用IE的标签式浏览试试看效果，这时打开的多个页面使用的都是同一个JS执行线程，如果其中一个页面在执行一个运算量较大的function时，其他窗口的JS就会停止工作）。

而异步机制是浏览器的两个或以上常驻线程共同完成的，例如异步请求是由两个常驻线程：JS执行线程和事件触发线程共同完成的，JS的执行线程发起异步请求（这时浏览器会开一条新的HTTP请求线程来执行请求，这时JS的任务已完成，继续执行线程队列中剩下的其他任务），然后在未来的某一时刻事件触发线程监视到之前的发起的HTTP请求已完成，它就会把完成事件插入到JS执行队列的尾部等待JS处理。又例如定时触发（settimeout和setinterval）是由浏览器的定时器线程执行的定时计数，然后在定时时间把定时处理函数的执行请求插入到JS执行队列的尾端（所以用这两个函数的时候，实际的执行时间是大于或等于指定时间的，不保证能准确定时的

```python
 import time

 def read(name, file) -> None:
    print(f"{name:<8} {time.strftime('%X')}")
    with open(file, 'r') as f:
        f.read()
    print(f"{name:<8} {time.strftime('%X')}")

def main() -> None:
    read('first',  'read/one_line_1.log')
    read('second', 'read/one_line_2.log')
    read('third',  'read/one_line_3.log')
 
if __name__ == '__main__':
    main()


first    10:43:57
first    10:44:01
second   10:44:01
second   10:44:05
third    10:44:05
third    10:44:08
```

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

var wg sync.WaitGroup

func Sum(name string, end int) {
    defer wg.Done()
    fmt.Println(name, end, time.Now())
    sum := 0
    for i := 0; i <= end; i++ {
        sum += i
    }
    fmt.Println(name, end, time.Now())
}

func main() {
    names := [...]string{"first", "second", "third"}
    delays := [...]int{15000000000, 1000000000, 13000000000}
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go Sum(names[i], delays[i])
    }
    fmt.Println("Over")
    wg.Wait()
}

// 异步执行 3 个百亿量级运算耗时 9s
third    20000000000 2022-11-22 10:51:36.4803571 +0800 CST m=+0.000173601
second   10000000000 2022-11-22 10:51:36.4804665 +0800 CST m=+0.000283101
first    15000000000 2022-11-22 10:51:36.4804039 +0800 CST m=+0.000220401
second   10000000000 2022-11-22 10:51:41.7277742 +0800 CST m=+5.247590701
first    15000000000 2022-11-22 10:51:43.8958834 +0800 CST m=+7.415699901
third    20000000000 2022-11-22 10:51:45.9174494 +0800 CST m=+9.437265801

// 异步执行单个百亿量级运算耗时 8s
third    20000000000 2022-11-22 10:51:00.7876033 +0800 CST m=+0.000169201
third    20000000000 2022-11-22 10:51:08.1227567 +0800 CST m=+7.335322701
```

3个线程同时运行, 相比单线程耗时更少

注: 多线程并行需要多个核心支持, 一般一个核心执行一个线程(存在超线程技术, 一个核心同时执行两个线程),  
线程刷量超过核心数量, 核心会在多个线程间来回切换执行

```javascript

const wait = async (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    setTimeout(() => {
        console.log(`${name} ${delay} ${(new Date()).toString()}`);
    }, delay*1000);
    console.log(`${name} Read Finish`)
}

const main = () => {
    wait("first ", 4);
    wait("second", 2);
    wait("third ", 6);
    console.log("Over")
}
  
main()

first  4 Wed Nov 23 2022 14:06:40 GMT+0800 (China Standard Time)
first  Read Finish
second 2 Wed Nov 23 2022 14:06:40 GMT+0800 (China Standard Time)
second Read Finish
third  6 Wed Nov 23 2022 14:06:40 GMT+0800 (China Standard Time)
third  Read Finish
Over
second 2 Wed Nov 23 2022 14:06:42 GMT+0800 (China Standard Time)
first  4 Wed Nov 23 2022 14:06:44 GMT+0800 (China Standard Time)
third  6 Wed Nov 23 2022 14:06:46 GMT+0800 (China Standard Time)
```
