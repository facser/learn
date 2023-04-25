# Golang

## Environment

[Golang 官网](https://go.dev/) 下载 Golang 最新的包
解压安装包到 /usr/local 目录下

```bash
 $ wget https://golang.google.cn/dl/go1.20.3.linux-amd64.tar.gz
 $ tar -zxvf go1.20.3.linux-amd64.tar.gz -C /usr/local/

 $ pwd                                           # 压缩包解压到 /usr/local/go 下
 > /usr/local/go
```

Golang 设置环境变量(二选一)

- 将 `/usr/local/go/bin` 添加进环境目录, 是目录下的可执行文件能被系统找到
- 创建 `/usr/local/go/bin` 文件下的可执行文件的软连接放到环境目录

本质是让系统在环境目录中找到 golang 的可执行文件

```bash
 $ export GOROOT=/usr/local/go                      # 将两条命令写入 ~/.bashrc
 $ export PATH=$PATH:$GOROOT/bin                    # 意为每次启动命令行都将 /usr/local/go/bin 加入环境目录

 $ ln -s /usr/local/go/bin/go  /usr/bin/go          # 将可执行文件 go 软连接放到环境变量
 > lrwxrwxrwx 1 root root 20 Dec 16 14:04 /usr/bin/go -> /usr/local/go/bin/go
```

## module

### go mod

使用 go mod 初始化项目, 并给项目命名
创建 main.go 文件为项目入口

```bash
 $ go mod init <module name>                     
 $ touch main.go

 $ ll
 > total 12K
 > -rw-r--r-- 1 root root   22 Mar 23 03:24 go.mod
 > -rw-r--r-- 1 root root 4.2K Apr 25 03:26 main.go

 $ cat go.mod
 > module learn
 >
 > go 1.20
```

往 main.go 添加代码

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println("hello world!")
}
```

执行 main.go

```bash
 $ go run main.go
 > hello world!
```

### import local module

使用 go mod 创建的项目, 会优先引入项目目录下的模块
本地目录不存在则会去 GOROOT 目录下寻找模块

```bash
demo
├── go.mod                                       # module learn  使用 go mod 在 demo 文件下创建 learn 项目
├── main.go                                      # package main  learn 项目的入口
└── lib                                          
    ├── config.go                                # package config 在 lib 下新建 config.go 隶属于 config 包
    └── flag.go                                  # package config 在 lib 下新建 flag.go 隶属于 config 包
```

在 main.go 引入 config 包

```go
import {
    "fmt"
    "learn/config"                               // <main module>/<import module> 
}

func main() {
    fmt.Println("import config")
    config.Head("title level 0", 0)              // 使用 config 包内的函数
}
```
