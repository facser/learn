# Mongo

## 示例

通过 docker 运行 mongo 数据库

```bash
 $ docker pull mongo
 $ docker images
 > REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
 > mongo        latest    32c5c1d795d9   2 weeks ago   644MB

 $ docker run -d --restart=always -p 27017:27017 --name mongodb -v /root/Desktop/Mongo:/data/db  mongo
 $ docker ps
 > CONTAINER ID   IMAGE  COMMAND                 CREATED        STATUS         PORTS                                           NAMES
 > b4da33977293   mongo  "docker-entrypoint.s…"  6 seconds ago  Up 5 seconds   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   mongodb
```

- 以 mongo 为镜像, 创建容器 mongodb, 
- 容器内 /data/db 目录挂载到系统 /root/Desktop/Mongo 目录下
- 系统端口 27017 与容器内 27017 端口映射

## mongo 容器

```bash
 $ docker exec -it mongodb bash 
 
 $ mongosh                                       # 进入 mongo shell, 早期版本使用 mongo 命令
 >
```

## 数据库

```js
 > show dbs                                      // 显示所有数据库
 admin    40.00 KiB
 config  108.00 KiB
 local    40.00 KiB
 test     40.00 KiB

 > use test                                      // 创建或切换数据库
 switched to db local

 > db                                            // 显示当前数据库名称
 local
···
