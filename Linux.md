<!--
 * @FilePath: \Learning\Linux.md
 * @Author: facser
 * @Date: 2022-07-18 15:02:16
 * @LastEditTime: 2022-07-18 17:18:35
 * @LastEditors: facser
 * @Description: 
-->
# Linux

[linux 命令](https://www.linuxcool.com/)

## 帮助和查找

[man](https://www.linuxcool.com/man)

```bash
 $ man <command>     # man (manual) 帮助手册, 查看命令的帮助手册
 $ man -f <command>  # 显示命令的简短描述

 $ man -k <command>  # 只记得部分命令, 列出所有含有字符的命令
```

[whatis](https://www.linuxcool.com/whatis)

```bash
 $ whatis <command> # 显示命令的简短描述, 等同于 man -f <command>
```

[info](https://wangchujiang.com/linux-command/c/info.html)

```bash
 $ info <command>   # 显示命令的 info 文档, 内容与帮助文档相似
```

[which](https://wangchujiang.com/linux-command/c/which.html)

```bash
 $ which <command>  # 查看命令所在位置
```

## 文件

### 常用目录

|位置|全称|说明|
|:-:|:-:|:-:|
|`/etc` |Configuration Files   |系统和软件的配置文件|
|`/usr` |Unix Software Resource|应用程序默认安装位置|
|`/dev` |Device Files          |系统外围设备|
|`/mnt` |Mount Directory       |空目录, 用于临时挂载文件系统|
|`/bin` |User Binaries         |所有用户可用的基本命令|
|`/home`|Home Directories      |普通用户的主目录|
|`/proc`|Process Information   |虚拟文件系统, 以映射系统与进程在内存中的信息|

### 文件操作

[mkdir](https://www.linuxcool.com/mkdir)

```bahs
 $ mkdir <dir>           # 创建目录

 $ mkdir -p <dir>/<dir>  # 创建多级目录
```