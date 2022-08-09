<!--
 * @FilePath: \文档\Learning\BASH\BASH-1-basic.md
 * @Author: facser
 * @Date: 2022-08-09 21:20:45
 * @LastEditTime: 2022-08-09 22:47:56
 * @LastEditors: facser
 * @Description: 
-->
# BASH

## BASH Basic

BASH 基础语法

### 命令

```bash
 $ command <opt> <args>                          # shell 命令一般格式

 $ cat -n log.txt                                # 命令 cat, 选项 -n, 参数 log.txt
```

shell 命令基本按照上述格式, 命令与选项, 参数之间以空格分割

### 打印输出

#### [echo](https://linux.alianga.com/c/echo.html)

```bash
 $ echo <string>                                 # 打印 string 内容
 $ echo -e <string>                              # 激活字符中的转义字符

 $ echo "first \nsecond"                        
 > first \nsecond

 $ echo -e "first \nsecond"                        
 > first 
 > second
```

#### [printf](https://linux.alianga.com/c/printf.html)

```bash
 $ printf <format string>                        # 格式化输出字符串

 $ printf "%s length is %.3f" "line" "4.53245"   # 字符串格式化 
 > line length is 4.523
```

### 变量引用

BASH 只有字符串一种数据类型, 想要操作字符串或者引用变量需要使用特殊符号

```bash
 $ varibal="hellow world"                        # 变量赋值, '=' 号前后不允许空格
 $ temp=hellow_world                             # 字符串无引号赋值时不允许空格

 $ echo varibal                                  # 把打印内容当做字符串直接打印 
 > varibal

 $ echo $varibal                                 # 打印变量的值 
 > hellow world                

 $ echo facser write ${temp}_baba                # 字符连用时, 用 {} 区分变量
 > facser write hellow_world_baba
```

建议字符串操作时, 添加引号使变量操作更加明确(易于区分编辑器中字符串与变量)








## 常用转义符号

|符号|含义|
|:--:|:--:|
|`\n`|换行符|
|`\r`|回车, 回到行首|
|`\t`|Tab 键|
|`\b`|光标左移 1 位|
