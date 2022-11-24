# 异步与多线程

## 介绍

- 阻塞
- 单线程与多线程
- 同步与异步

### 阻塞

- I/O bound
- CPU bound

```bash

time |------ Device I/O ------|-- other --|
             long time          short time

data <- CPU <- data -> Memory <- data -> device(Disk NIC) 
     ^          ^                 ^
    fast      slowly            slowly   
```
I/O bound: I/O 密集操作, CPU 大部分时间在等硬盘和内存 I/O, CPU loading 低 
I/O bond 因为外部设备瓶颈无法发挥 CPU 性能

```bash
time |------ CPU operation ------|-- other --|
             long time             short time
```
CPU bound: CPU 密集操作, CPU 大部分时间处于运算中, CPU loading 高
I/O bond 因为 CPU 瓶颈无法发挥外部设备性能


上述两种情况由于单方面瓶颈无法发挥机器整体性能
为了充分发挥机器的性能, 衍生了多线程和异步技术

```javascript

// 同步读取文件
const readSync = (name, file) => {
    console.log(`${name} ${(new Date()).toString()}`);
    require("fs").readFileSync(file);
    console.log(`${name} ${(new Date()).toString()}`);
}

// 异步读取文件
const readAsync = (name, file) => {
    console.log(`${name} ${(new Date()).toString()}`);
    require('fs').readFile(file, () => {
        console.log(`${name} ${(new Date()).toString()}`);
    });
    console.log(`${name} Read Finish`)
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

// 同步读取 3 个文件消耗 30s 
first  Wed Nov 23 2022 16:44:21 GMT+0800 (China Standard Time)
first  Wed Nov 23 2022 16:44:31 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 16:44:31 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 16:44:41 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 16:44:41 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 16:44:51 GMT+0800 (China Standard Time)

// 异步读取同样 3 个文件消耗 17s
first  Wed Nov 23 2022 16:44:51 GMT+0800 (China Standard Time)
first  Read Finish
second Wed Nov 23 2022 16:44:51 GMT+0800 (China Standard Time)
second Read Finish
third  Wed Nov 23 2022 16:44:51 GMT+0800 (China Standard Time)
third  Read Finish
third  Wed Nov 23 2022 16:45:01 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 16:45:03 GMT+0800 (China Standard Time)
first  Wed Nov 23 2022 16:45:08 GMT+0800 (China Standard Time)
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

### 单线程与多线程

多个线程同时运行

```python
import time
from threading import Thread
    
def wait(name:str, delay:int):
    print(f"{name:<8} {delay} {time.strftime('%X')}")
    time.sleep(delay)
    print(f"{name:<8} {delay} {time.strftime('%X')}")
    
def main() -> None:
    first:Thread  = Thread(target=wait, args=('first', 4))
    second:Thread = Thread(target=wait, args=('second', 2))
    third:Thread  = Thread(target=wait, args=('third', 6))
    
    [p.start() for p in (first, second, third)]
    [p.join() for p in (first, second, third)]
  
if __name__ == '__main__':
    main()

first    4 14:26:15
second   2 14:26:15
third    6 14:26:15
second   2 14:26:17
first    4 14:26:19
third    6 14:26:21
```

3个线程同时运行, 相比单线程耗时更少

注: 多线程需要多个核心支持, 一般一个核心执行一个线程(存在超线程技术, 一个核心同时执行两个线程),  
线程刷量超过核心数量, 核心会在多个线程间来回切换执行

### 同步与异步

同步:
同步执行代码时是顺序逐行执行的, 必须执行当前代码后才能继续执行下一行
同步代码有确定的执行顺序
同步代码遇到文件 I/O 或网络 I/O 会产生阻塞

```python
 import time
 

 print(f"start at {time.strftime('%X')}")
 time.sleep(5)
 time.sleep(3)
 print(f"close at {time.strftime('%X')}")

 start at 10:56:24
 close at 10:56:32
```

异步:
执行遇到异步操作会直接返回, 继续执行后续代码, 待异步操作完成后, 主线程能收到消息
异步的执行顺序与代码顺序不一定一致
异步操作之间无数据依赖, 可以独立执行

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

异步能跳过阻塞操作, 执行后续内容, 待阻塞操作完成将回调函数插入主线程执行

## 异步实现

### 多线程异步

主线程跳过异步操作, 新开线程执行跳过的操作, 使主线程运行达到异步效果


1. Golang 多线程异步

```Go
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
	wg.Wait()                                                                      
}


Over
third    5 2022-11-21 10:26:36.9768235 +0800 CST m=+0.000138501
second   3 2022-11-21 10:26:36.9770264 +0800 CST m=+0.000341101
first    4 2022-11-21 10:26:36.9770273 +0800 CST m=+0.000341901
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

2. Python 多线程异步

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

# 异步执行 3 个演示函数和 3 千万量级的运算
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

# 执行单个千万量级的运算
first    40000000 16:45:38
first    40000000 16:45:41                               

second   20000000 16:46:13
second   20000000 16:46:15                             

third    60000000 16:46:32
third    60000000 16:46:36                                
```
> 注解 由于 GIL 的存在, asyncio.to_thread() 通常只能被用来将 IO 密集型函数变为非阻塞的.
> 对于会释放 GIL 的扩展模块或无此限制的替代性 Python 实现来说, asyncio.to_thread() 也可被用于 CPU 密集型函数.(多进程, 或无 GIL 的 Python)

### 单线程异步

单线程异步在遇到阻塞时挂起该操作, 等阻塞操作完成后通过回调函数或通知回到线程运行

```javascript
// 异步读取文件
const readAsync = (name, file) => {
    console.log(`${name} ${(new Date()).toString()}`);
    require('fs').readFile(file, () => {
        console.log(`${name} ${(new Date()).toString()}`);
    });
    console.log(`${name} Read Finish`)
}

const main = () => {
    readAsync("first ", "read/one_line_1.log")
    readAsync("second", "read/one_line_2.log")
    readAsync("third ", "read/one_line_3.log")
}

main()


first  Wed Nov 23 2022 11:30:06 GMT+0800 (China Standard Time)
first  Read Finish
second Wed Nov 23 2022 11:30:06 GMT+0800 (China Standard Time)
second Read Finish
third  Wed Nov 23 2022 11:30:06 GMT+0800 (China Standard Time)
third  Read Finish
first  Wed Nov 23 2022 11:30:11 GMT+0800 (China Standard Time)
third  Wed Nov 23 2022 11:30:13 GMT+0800 (China Standard Time)
second Wed Nov 23 2022 11:30:14 GMT+0800 (China Standard Time)
```

## 多语言异步对比

### Javascript

仅支持单线程异步, 能有效节省文件 I/O 和网络 I/O 时间
因为只有单线程, 无法节省 CPU 密集型操作时间

```javascript

const record = (name, delay) => {
    console.log(`${name} ${delay} ${(new Date()).toString()}`);
    let promise = new Promise((resolve) => {
        let sum = 0;
        for (let i=0; i<delay; i++) {
            sum += i;
        };
        resolve(`${name} ${delay} ${(new Date()).toString()}`);
    });
    console.log(`${name} Finish`)
    return promise;
};

const main = () => {
    record("first ", 3000000000).then(msg => console.log(msg));
    record("second", 2000000000).then(msg => console.log(msg));
    record("third ", 4000000000).then(msg => console.log(msg));
    console.log("Over")
}
  
main()

// 异步执行 3 个十亿量级运算
first  3000000000 Wed Nov 23 2022 15:23:28 GMT+0800 (China Standard Time)
first  Finish
second 2000000000 Wed Nov 23 2022 15:23:31 GMT+0800 (China Standard Time)
second Finish
third  4000000000 Wed Nov 23 2022 15:23:33 GMT+0800 (China Standard Time)
third  Finish
Over
first  3000000000 Wed Nov 23 2022 15:23:31 GMT+0800 (China Standard Time)
second 2000000000 Wed Nov 23 2022 15:23:33 GMT+0800 (China Standard Time)
third  4000000000 Wed Nov 23 2022 15:23:38 GMT+0800 (China Standard Time)


// 异步执行 1 个十亿量级的运算
third  4000000000 Wed Nov 23 2022 15:24:04 GMT+0800 (China Standard Time)
third  Finish
Over
third  4000000000 Wed Nov 23 2022 15:24:09 GMT+0800 (China Standard Time)

// 同步执行 1 个十亿量级的运算
third  4000000000 Wed Nov 23 2022 15:26:31 GMT+0800 (China Standard Time)
third  4000000000 Wed Nov 23 2022 15:26:36 GMT+0800 (China Standard Time)
Over
```

### Python

Python 支持单线程多线程异步, 能节省文件 I/O 和网络 I/O 时间 
由于进程中 GIL 存在, 每个进程同一时间点仅允许一个线程执行

Python 单个进程中的多线程实际是多个线程快速来回切换, 不省 CPU 计算时间

```python
first    40000000 15:27:18                       
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

Python 多进程是可以利用多核心同时执行

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

### Golang

Golang 支持多线程异步, 使用 GPM 模型自动化分配协程到线程上执行

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

// 异步执行 3 个百亿量级运算
third    20000000000 2022-11-22 10:51:36.4803571 +0800 CST m=+0.000173601
second   10000000000 2022-11-22 10:51:36.4804665 +0800 CST m=+0.000283101
first    15000000000 2022-11-22 10:51:36.4804039 +0800 CST m=+0.000220401
second   10000000000 2022-11-22 10:51:41.7277742 +0800 CST m=+5.247590701
first    15000000000 2022-11-22 10:51:43.8958834 +0800 CST m=+7.415699901
third    20000000000 2022-11-22 10:51:45.9174494 +0800 CST m=+9.437265801

// 异步执行单个百亿量级运算
third    20000000000 2022-11-22 10:51:00.7876033 +0800 CST m=+0.000169201
third    20000000000 2022-11-22 10:51:08.1227567 +0800 CST m=+7.335322701
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