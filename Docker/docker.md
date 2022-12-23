# Docker

## 介绍

开发的时候经常遇到环境配置的问题, 从网上克隆下来的项目必须保证项目需要的依赖已安装且不与本地冲突才能正常运行

- 安装所有项目依赖
- 与本地环境隔离
- 轻量化

docker 就符合以上需求, docker 能在当前环境下快速生成一个与当前环境隔离的容器, 容器类似一个轻量化的虚拟机,
容器环境可自定义, 仅安装需要使用的包即可

## 安装与配置

- 安装
- 配置

1. 

```bash
# 安装依赖
apt update && apt -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common

# 安装 GPG 证书
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/debian/gpg | sudo apt-key add

# 添加 docker 软件源
add-apt-repository "deb [arch=amd64] https://mirrors.bfsu.edu.cn/docker- ce/linux/debian $(lsb_release -cs) stable"

# 更新软件源泉, 下载安装 docker
apt update && apt -y install docker-ce
```

2. 配置

```bash
docker info                                                                    # 显示 docker 相关信息

docker version                                                                 # 显示 docker 版本详细信息

docker --version                                                               # 显示 docker 版本信息

systemctl status docker                                                        # 查看 docker 运行详细状态
service docker status                                                          # 查看 docker 运行状态
```

编辑 `/etc/docker/daemon.json`(不存在则创建一个), 使用 `man dockerd` 或官方文档查看参数使用说明  
[官方文档](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon)

```bash
{
    "insecure-registries": ["192.168.2.2:8080"],                               # 私有镜像仓库, 第三方镜像源 "<IP>:<PORT>"
    "dns": [],                                                                 # 设定容器DNS的地址，在容器的 /etc/resolv.conf文件中可查看
    "exec-opts": ["native.cgroupdriver=systemd"],                              # 运行时执行选项
    "registry-mirrors": ["https://ucjisdvf.mirror.aliyuncs.com"],              # 更换官方镜像仓库地址为国内镜像地址
    "log-level": "info",                                                       # 显示日志等级 (debug|info|warn|error|fatal, 默认为 info)
    "log-driver": "json-file",                                                 # log 驱动
    "log-opts": {                                                              # 容器默认日志驱动程序选项
        "max-size": "100m", 
        "max-file": "3" 
    },
    "data-root": "/var/lib/docker"                                             # docker 运行及日志保存位置 (默认 /var/lib/docker)
    }
```

修改配置文件后需要重启 docker 服务生效

```bash
service docker restart

systemctl restart docker
```

## 镜像

docker 容器是以镜像为模板生成的实例, 镜像和容器可类比为面向对象中的类和对象

- 单个镜像可以生成多个容器
- 可以自定义镜像环境

### 镜像操作

- 获取镜像
- 镜像列表
- 删除镜像

1. 获取镜像

```bash
 $ docker search [IMAGE NAME]
 $ docker search ubuntu

 > NAME                             DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
 > ubuntu                           Ubuntu is a Debian-based Linux operating sys…   15360               [OK]    

 $ docker pull [OPTIONS] NAME[:TAG|@DIGEST]
 $ docker pull ubuntu:20.04                                                    # 获取官方 ubuntu 20.04 版本镜像 (TAG 默认 latest)
 $ docker pull registry.ipt-gitlab:8081/ta-web/sit-db-mongo/mongo-base:1.0.0   # 拉取私有仓库的 mongo-base 镜像 tag: 1.0.0
```

|选项|含义|
|:-:|:-|
|`NAME`|镜像名称|
|`DESCRIPTION`|镜像名称|
|`STARS`|点赞数|
|`OFFICIAL`|是否官方|
|`AUTOMATED`|是否自动构建|

1. 镜像列表

```bash
 $ docker images [OPTIONS] [REPOSITORY[:TAG]]

 $ docker images                                                               # 列出所有镜像
 $ docker images -q, --quite                                                   # 仅显示镜像 ID

 >REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
 >ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
```

|选项|含义|
|:-:|:-:|
|`REPOSITORY`|镜像仓库源|
|`TAG`|镜像 tag|
|`IMAGE ID`|镜像 ID|
|`CREATED`|镜像创建时间|
|`SIZE`|镜像大小|

3. 删除镜像

```bash
 $ docker image save [OPTIONS] IMAGE [IMAGE...]
 $ docker image save centos > docker-centos.tar.gz

 $ docker rmi [OPTIONS] IMAGE [IMAGE...]
```

### 自定义镜像

- Dockerfile
- 自定义镜像

```docker
FROM ubuntu                                                                    # 以 ubuntu 镜像为基础, 可添加 tag, ubuntu:20.04

LABEL version="1.0.0" description="ubuntu image"                               # 添加镜像元数据

ENV path=/usr/local/                                                           # 设置全局变量, 可添加多个，或 ENV 多次设置, 可以使用已设置的变量

ADD nginx-1.8.0.tar.gz $path                                                   # 将系统下文件复制到镜像中目录下
ADD epel-release-latest-7.noarch.rpm $path 

WORKDIR $path                                                                  # 设定镜像中工作目录, 并转到改目录, 类似 cd 命令, 可以多次设置

RUN rpm -ivh /usr/local/epel-release-latest-7.noarch.rpm &&\                     # 执行 shell 命令
    yum install -y wget lftp gcc gcc-c++ make openssl-devel pcre-devel pcre &&\ 
    yum clean all &&\
    cd $path/nginx-1.8.0 &&\
    ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre &&\
    make &&\
    make install &&\
    echo "daemon off;" >> /etc/nginx.conf 

CMD /usr/sbin/nginx                                                                # 生成容器后执行的命令, 会被 docker run 生成容器时初始命令覆盖
```

```docker
ARG <name>[=<default value>]                                                   # 设置构建镜像的外部参数, 修改参数需要使用 --build-arg

ARG USERNAME="facser"                                                          # Dockerfile 设置默认参数 "facser"

docker build --build-arg USERNAME="kertory" -t demo:v1                         # build 镜像时通过 --build-arg 修改 USERNAME 的值
```

```docker
RUN <command>                                                                  # 通过 sh 执行命令
RUN ["executable", "param1", "param2"]                                         # 指定 shell 执行命令

RUN date                                                                       # 通过 sh 执行 date 命令 (命令执行失败即停止)
RUN ["/bin/sh", "-c", "date"]                                                  # 和上命令完全一致
RUN ["/bin/bash", "-c", "date"]                                                # 通过 bash 执行 date 命令 (命令执行失败继续执行)

RUN echo "line first"  >> /root/run.log                                        # 执行 3 个 RUN 指令, 创建 3 个镜像层 
RUN echo "line second" >> /root/run.log                                        # 层数越多占用空间更大
RUN echo "line third"  >> /root/run.log                                        # 创建失败时, 从失败的上一层 RUN 继续, 重新创建速度更快

RUN echo "line first"  >> /root/run.log &&\                                    # 一个 RUN 指令创建 1 个镜像层
    echo "line second" >> /root/run.log &&\                                    # 只有一层镜像, 占用更小
    echo "line third"  >> /root/run.log                                        # 每次创建都需要从头开始执行
```



```bash
 docker build [OPTIONS] PATH | URL | -

 Options:
   --file, -f                                                                  # 指定要使用的Dockerfile路径；
   --tag, -t                                                                   # 镜像的名字及标签(name:tag 或 name, 允许多个) 
   --no-cache                                                                  # 不使用缓存


 $ docker build -t demo:v1  .                                                 
 
 $ docker build -t demo:v2 -f /root/Dockerfile 
```



## 容器

### 容器操作

1. 容器列表

```bash
 $ docker ps [OPTIONS]                           # 显示容器列表及相关信息

 $ docker ps
 $ docker ps -a, --all                           # 显示所有容器, 包括未运行的
 $ docker ps -s, --size                          # 显示正在运行的容器, 显示容器大小
 $ docker ps -q, --quite                         # 仅显示容器 ID
 
```

|选项|含义|
|:-:|:-:|
|`CONTAINER ID`|容器 ID|
|`IMAGE`       |生成容器的镜像|
|`COMMAND`     |启动容器时运行的命令|
|`CREATED`     |容器创建时间|
|`STATUS`      |容器状态|
|`PORTS`       |容器端口和链接类型|
|`NAMES`       |容器名称|
|`SIZE`        |容器大小|


2. 操作容器

```bash
 docker stop    <CONTAINER ID | NAMES>                                         # 关闭容器
 docker start   <CONTAINER ID | NAMES>                                         # 启动容器
 docker kill    <CONTAINER ID | NAMES>                                         # 杀死容器进程
 docker restart <CONTAINER ID | NAMES>                                         # 重启容器
 docker rm -f   <CONTAINER ID | NAMES>                                         # 强制删除容器(运行中的容器也会删除) 

 docker logs    <CONTAINER ID | NAMES>                                         # 显示指定容器 log
 docker top     <CONTAINER ID | NAMES>                                         # 列出指定容器进程
 docker port    <CONTAINER ID | NAMES>                                         # 显示容器的端口映射
```

1. 创建容器
   
```bash
Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Options:
  -d, --detach                                                                 # 后台运行容器，并输出容器ID
  -e, --env list                                                               # 设置环境变量，该变量可以在容器内使用
  -h, --hostname string                                                        # 指定容器的hostname
  -i, --interactive                                                            # 以交互模式运行容器，通常与-t同时使用
  -l, --label list                                                             # 给容器添加标签
  --name <name>                                                                # 设置容器名称，否则会自动命名
  --network string                                                             # 将容器加入指定网络
  -p, --publish list                                                           # 设置容器映射端口
  -P,--publish-all                                                             # 将容器设置的所有exposed端口进行随机映射
  --restart <restart option>                                                   # 容器重启策略，默认为不重启
    on-failure[:max-retries]：                                                   # 在容器非正常退出时重启，可以设置重启次数。
    unless-stopped：                                                             # 总是重启，除非使用stop停止容器
    always：                                                                     # 总是重启
  --rm                                                                         # 容器退出时则自动删除容器
  -t, --tty                                                                    # 分配一个伪终端
  -u, --user <username>                                                        # 运行用户或者UID
  -v, --volume list                                                            # 数据挂载
  -w, --workdir <work path>                                                    # 容器的工作目录
  --privileged                                                                 # 给容器特权

```

```bash
 $ docker run -it --rm ubuntu bash                                             # 以 ubuntu 镜像创建容器(自动命名), 创建后执行 bash, 退出后自动删除容器 
 $ docker run -itd -p 8589:27017 --name demo mongo                             # 以 mongo 镜像创建名为 demo 容器, 后台运行, 机器 8589 端口映射到容器 27017 端口

❯ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
ee0c15a3a0ee        mongo               "docker-entrypoint.s…"   13 seconds ago      Up 11 seconds       0.0.0.0:8589->27017/tcp   demo
```

```bash
 $ docker attach [OPTIONS] CONTAINER
 $ docker attach ff8b371b77b9

 $ docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
 $ docker exec -it ff8b371b77b9 bash
```
