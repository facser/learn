<!--
 * @FilePath: \文档\Learning\Linux\Linux-2-file.md
 * @Author: facser
 * @Date: 2022-07-18 15:02:16
 * @LastEditTime: 2022-08-08 21:44:26
 * @LastEditors: facser
 * @Description: 
-->

# Linux File

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

### 特殊文件

|位置|说明|
|:-|:-:|
|`/etc/environment`                    |任意用户打开命令行加载, 系统环境变量|
|`/etc/profile`                        |任意用户打开命令行加载|
|`/etc/bash.bashrc`                    |任意用户打开命令行加载|
|`~/.profile`                          |当前用户打开命令行时执行的文件|
|`~/.bashrc`                           |当前用户打开命令行时执行的文件|
|`/ect/rc.d/rc.local`                  |系统启动时执行的文件(centos, redhat)|
|`/lib/systemd/system/rc-local.service`|系统启动时执行的文件(Ubuntu)|

注: 打开命令行加载顺序和表格顺序一致

### Root 用户

```bash
 $ sudo passwd root
 > Enter new UNIX password:                      # 设置 root 用户密码
 > Retype new UNIX password:                     # 重复输入 root 密码
 > passwd: password updated successfully         # 设置成功

 $ su root                                       # 切换 root 用户
\# exit                                          # 退出 root, 普通用户 $, root 用户 #

 $ su <user>                                     # 切换用户
```

### 文件查看

#### [tree](https://www.linuxcool.com/tree)

```bash
 $ tree                                          # 显示目录的树状层级图
 $ tree -f                                       # 树状图显示绝对路径
```

#### [pwd](https://www.linuxcool.com/pwd) :  print working directory

#### [dirs](https://www.linuxcool.com/dirs) : directories

```bash
 $ pwd                                           # 显示当前路径
 $ dirs                                          # 显示当前路径
```

#### [ls](https://www.linuxcool.com/ls) : list files

```bash
 $ ls                                            # 显示当前目录下所有文件及目录
 $ ls -a                                         # --all 额外显示隐藏文件及目录
 $ ls -l                                         # 使用长格式显示文集及目录详细信息
 $ ls -R                                         # --recursive 递归显示所有子目录
 $ ls -S                                         # sort 根据文件大小排序

 $ ls -alS                                       # 参数可无顺序合并, 结果按参数显示
```

#### [file](https://linux.alianga.com/c/file.html)

```bash
 $ file <file>                                                  # 显示文件类型
 > a.py: Python script, UTF-8 Unicode text executable           # 文件名, 类型, 编码类型
```

### 文件操作

#### [cd](https://www.linuxcool.com/cd) : change directory

```bash
 $ cd <dir>                                      # 切换到 <dir> 目录

 $ cd ..                                         # 返回上级目录
 $ cd -                                          # 回到上次所有在目录
 
```

#### [mkdir](https://www.linuxcool.com/mkdir) : make directories

```bash
 $ mkdir <dir>                                   # 创建目录

 $ mkdir -p <dir>/<dir>                          # 创建多级目录
```

#### [touch](https://www.linuxcool.com/touch)

```bash
 $ touch <file> <file>                           # 文件不存在, 创建文件, 可同时创建多个
 $ touch <file>                                  # 文件存在, 修改文件读取和修改时间
```

#### [rm](https://www.linuxcool.com/rm) :  remove

```bash
 $ rm -f                                         # --force 强制删除文件, 不询问
 $ rm -r                                         # -R, --recursive 递归删除, 删除文件夹及下所有文件
 $ rmdir                                         # 删除空目录, 目录下有文件或文件夹报错
```

#### [mv](https://linux.alianga.com/c/mv.html) : move

```bash
 $ mv <file|dir> <file|dir>                      # 剪切复制并重新命名, 文件目录均可
 $ mv file_name  dir/                            # 保存文件名移动

 $ mv -v                                         # --verbose 显示过程, 打印原名及更改后名
 $ mv -f                                         # --force 强制移动, 存在同名则覆盖
 $ mv -n                                         # --no-clobber 存在同名文件则不移动
 
 $ mv -bv a.log  b.log                           # backup 备份移动, 存在同名时, 修改改名同名文件名 
 > renamed 'a.log' -> 'b.log' (backup: 'b.log~')
```

#### [cp](https://wangchujiang.com/linux-command/c/cp.html) : copy

```bash
 $ cp <file|dir> <file|dir>                      # 复制黏贴重命名

 $ cp -v                                         # --verbose 显示详细过程
 $ cp -f                                         # --force 强制复制, 存在同名直接覆盖
 $ cp -r                                         # -R, --recursive 递归复制
 $ cp -b                                         # backup 存在同名文件时, 目标文件改名

 $ cp -l                                         # --link 创建源文件的硬链接
 $ cp -s                                         # --symbolic-link 创建源文件的符号链接

 $ ln <file> <file>                              # 创建文件的硬链接
 $ ln -s <file> <file>                           # --symbolic 创建文件的符号链接
```

- 硬链接: 一个数据绑定两个名字, 两名字都删除才无法访问数据
- 符号链接: 数据的"软链接" "快捷方式", 只是一个链接, 不含数据

### 文件查找

#### [find](https://wangchujiang.com/linux-command/c/find.html)

```bash
 $ find <dir> <options>                          # 列出在 <dir> 下符合参数的文件或目录(绝对路径)

 $ find ~/Desktop -name *.py                     # 在 ~/Desktop 所有后缀为 .py 的文件
 $ find . -path *lib*                            # 在当前目录所有绝对地址中含有 'lib' 的文件或目录
 $ find lib/ -regex ".*\.txt$"                   # lib 目录下符合正则表达式的文件

 $ find <dir> <options> -exec <cmd> {} \;        # 对查找到的文件进行操作
 $ find . -name *.sh -exec rm {} \;              # 删除当前目录下后缀为 .sh 文件
 $ find . -name *.py -exec mv {} /tmp \;         # 将当前目录下后缀为 .py 文件移动到 /tmp
```

#### [locate](https://www.linuxcool.com/locate)

```bash
 $ locate <file|dir>                             # 列出 / 目录下所有含 <file|dir> 的文件或目录

 $ locate -c                                     # --count 显示查找出的文件数量
```

### 文件查看

#### [cat](https://www.linuxcool.com/cat) : concatenate

```bash
 $ cat <file>                                    # 读取并打印文件内容
 $ cat -n <file>                                 # 打印文件内容并添加行数
```

#### [head](https://www.linuxcool.com/head)

```bash
 $ head <file>                                   # 显示文件的前 10 行
 $ head -n 5 <file>                              # --lines 显示文件前 5 行
 $ head -c 20 <file>                             # --bytes 显示文件前 20 个字符 
```

#### [tail](https://www.linuxcool.com/tail)

```bash
 $ tail <file>                                   # 显示文件的后 10 行
 $ tail -n 5 <file>                              # --lines 显示文件后 5 行
 $ tail -c 20 <file>                             # --bytes 显示文件最后 20 个字符 
```
