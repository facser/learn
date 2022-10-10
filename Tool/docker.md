# Docker

## 介绍

开发的时候经常遇到环境配置的问题, 从网上克隆下来的项目必须保证项目需要的依赖已安装且不与本地冲突才能正常运行

- 安装所有项目依赖
- 与本地环境隔离
- 轻量化

docker 就符合以上需求, docker 能在当前环境下快速生成一个与当前环境隔离的容器, 容器类似一个轻量化的虚拟机,
容器环境可自定义, 仅安装需要使用的包即可

## 镜像

docker 容器是以镜像为模板生成的实例, 镜像和容器可类比为面向对象中的类和对象

- 单个镜像可以生成多个容器
- 镜像环境可以自定义

### 镜像操作

- 获取镜像
- 镜像列表
- 删除镜像

```bash
 $ docker pull [OPTIONS] NAME[:TAG|@DIGEST]

 $ docker pull ubuntu:20.04                      # 获取镜像
```

```bash
 $ docker images [OPTIONS] [REPOSITORY[:TAG]]

 $ docker images                                 # 列出所有镜像
 $ docker images -q, --quite                     # 仅显示镜像 ID

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

```bash
 $ docker rmi [OPTIONS] IMAGE [IMAGE...]

```

### 自定义镜像

自定义镜像

```docker
 docker build [OPTIONS] PATH | URL | -
```

## 容器

### 容器操作

```bash
 $ docker ps [OPTIONS]                           # 显示容器列表及相关信息

 $ docker ps
 $ docker ps -a, --all                           # 显示所有容器, 包括未运行的
 $ docker ps -s, --size                          # 显示容器大小
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


```bash
 docker stop <CONTAINER ID | NAMES>
 docker kill <CONTAINER ID | NAMES>
 docker restart <CONTAINER ID | NAMES>
 docker rm -f <CONTAINER ID | NAMES>
```

```bash
 $ docker logs [OPTIONS] CONTAINER

 $ docker logs <NAMES | CONTAINER ID>
```

### docker run