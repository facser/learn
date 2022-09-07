<!--
 * @FilePath: \文档\Learning\Linux\Linux-1-basic.md
 * @Author: facser
 * @Date: 2022-07-27 21:20:25
 * @LastEditTime: 2022-07-28 22:22:43
 * @LastEditors: facser
 * @Description: 
-->
# Linux Basic

[linux 命令](https://www.linuxcool.com/)

### 帮助和查找

#### [man](https://www.linuxcool.com/man) : manual

```bash
 $ man <command>                                 # man (manual) 帮助手册, 查看命令的帮助手册
 $ man -f <command>                              # 显示命令的简短描述

 $ man -k <command>                              # 只记得部分命令, 列出所有含有字符的命令
```

#### [whatis](https://www.linuxcool.com/whatis)

```bash
 $ whatis <command>                              # 显示命令的简短描述, 等同于 man -f <command>
```

#### [info](https://wangchujiang.com/linux-command/c/info.html)

```bash
 $ info <command>                                # 显示命令的 info 文档, 内容与帮助文档相似
```

#### [which](https://wangchujiang.com/linux-command/c/which.html)

```bash
 $ which <command>                               # 查看命令所在位置
```

#### [history](https://linux.alianga.com/c/history.html)

```bash
 $ history                                       # 查看执行的命令历史

 $ !!                                            # 执行上一条命令
```

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

sudo 免密码

```bash
 $ sudo vi /etc/sudoers                          # 编辑配置文件

 > %sudo ALL=(ALL:ALL) ALL                       # 找到这一栏, 建议注释掉复制一行修改
 > %sudo ALL=(ALL:ALL) NOPASSWD:ALL              # 修改后, 强制保存退出
```

注: 该文件必须强制写入, 不能修改文件权限, 否则报错

### 通配符号

#### `？` 任意单个字符

```bash
 $ touch ab a bc abc                             # 生成 ab a ba abc 4 个文件
 
 $ ls ?b                                         # ? 可以指代任意单个字符
 > ab

 $ ls b?
 > bc
```

#### `*` 任意多个字符

```bash
 $ touch ab a bc abc                             # 生成 ab a ba abc 4 个文件
 
 $ ls *                                          # * 可以指代任意多个字符
 > a  ab  abc  bc

 $ ls a*                                    
 > a  ab  abc
```

#### `**` 任意多级目录

```bash
 $ cat /etc/**/word                               # /etc/ 文件夹下所有 word 文件
```

#### `[]` 匹配范围

```bash
 $ touch aa ab ac aab                            # 生成 ab a ba abc 4 个文件

 $ ls a[ab]                                      # 匹配 [] 内任意一个字符
 > aa ab
```

#### 特殊符号

#### `|` 管道符号

```bash
 $
```

#### `>` `>>` `<` 重定向

```bash
 $ <cmd> > <file>                                # 将输出覆盖写入文件(原文件清空后写入)
 $ ls > file.log                                 # 将 ls 命令返回值写入 file.log 文件

 $ <cmd> >> <file>                               # 将输出追加写入文件(原文件内容保留)
 $ ls > file.log                                 # 将 ls 命令返回值写入 file.log 内容结尾

 $ <cmd> < <file>                                # 将文件内容重定向为标准输入
 $ cat < file.log                                # 读取 file.log 并打印
```

#### `&1` `&2` `/dev/null` 输出

```bash
 $ ls  2>&1                                      # 错误输出重定向到标准输出 

 $ ls  >/dev/null                                # 不显示结果
```

### 单词缩写

|缩写|全称|翻译|
|:-:|:-:|:-:|
|h    |`help`             |帮助|
|a    |`all`              |全部|
|f    |`force`            |强制|
|i    |`interactive`      |交互的|
|b    |`backup`           |备份|
|v    |`version / verbose`|版本/详细的|
|c    |`count / command`  |计数/命令|
|r / R|`recursive`        |递归|
|s / S|`sort`             |排序|

### 特殊符号

|符号|含义|
|:-: |:-|
|`|` |管道符号, 正则中 或|
|`>` |输出重定向, 覆盖|
|`>>`|输出重定向, 追加|
|`&` |程序放入后台执行|
|`#` |注释|
|`&&`|且, 左边成功才执行右边|
|`||`|左边不影响右边执行|

### 正则表达式

|符号|模式|
|:-:     |:-|
|`^`     |锚定行首|
|`$`     |锚定行尾|
|`()`    |捆绑成一个整体|
|`.`     |任意一个字符|
|`?`     |前面字符或模式 0 或 1 次|
|`{m}`   |前面字符或模式 m 次|
|`{m, n}`|前面字符或模式次数在 m n 之间|
|`+`     |前面字符或模式 1 次或多次|
|`*`     |前面字符或模式任意次|
|`|`     |或选择|
|`[]`    |括号范围内均可|
|`[^]`   |括号范围之外均可|
