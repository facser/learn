<!--
 * @FilePath: \文档\Learning\Linux\Linux-1-basic.md
 * @Author: facser
 * @Date: 2022-07-27 21:20:25
 * @LastEditTime: 2022-07-27 21:31:53
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
