<!--
 * @FilePath: \文档\Learning\Linux.md
 * @Author: facser
 * @Date: 2022-07-18 15:02:16
 * @LastEditTime: 2022-07-18 22:43:14
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

### 文件查看

[tree](https://www.linuxcool.com/tree)

```bash
 $ tree                  # 显示目录的树状层级图
 $ tree -f               # 树状图显示绝对路径

```

[pwd](https://www.linuxcool.com/pwd) :  print working directory
[dirs](https://www.linuxcool.com/dirs) : directory

```bash
 $ pwd                   # 显示当前路径
 $ dirs                  # 显示当前路径
```

[ls](https://www.linuxcool.com/ls) : list

```bash
 $ ls                    # 显示当前目录下所有文件及目录
 $ ls -a                 # 额外显示隐藏文件及目录
 $ ls -l                 # 使用长格式显示文集及目录详细信息
 $ ls -R                 # 递归显示所有子目录
 $ ls -S                 # 根据文件大小排序

 $ ls -alS               # 参数可无顺序合并, 结果按参数显示
```

### 文件操作

[cd](https://www.linuxcool.com/cd) : change directory

```bash
 $ cd <dir>           # 切换到 <dir> 目录

 $ cd ..              # 返回上级目录
 $ cd -               # 回到上次所有在目录
 
```

[mkdir](https://www.linuxcool.com/mkdir) : make directories

```bash
 $ mkdir <dir>           # 创建目录

 $ mkdir -p <dir>/<dir>  # 创建多级目录
```

[rm](https://www.linuxcool.com/rm) :  remove

```bash
 $ rm -f                 # 强制删除文件, 不询问
 $ rm -r                 # 递归删除, 删除文件夹及文件夹下所有文件

 $ rmdir                 # 删除空目录, 目录下有文件或文件夹报错
```

[mv](https://linux.alianga.com/c/mv.html) : move

```bash
 $ mv <file|dir> <file|dir>      # 剪切复制并重新命名, 文件目录均可
 $ mv file_name  dir/            # 保存文件名移动

 $ mv -v                         # 显示过程, 打印原名及更改后名
 $ mv -f                         # 强制移动, 存在同名则覆盖
 $ mv -n                         # 存在同名文件则不移动
 
 $ mv -bv a.log  b.log           # 备份移动, 存在同名时, 修改改名同名文件名 
 > renamed 'a.log' -> 'b.log' (backup: 'b.log~')
```

[cp]()

```bash
 $
```

### 文件查找

[find]()

```bash
 $
```

