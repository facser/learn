# Linux Text

## 文本搜索

读取文本内容搜索或刷选符合条件的内容

### [grep](https://linux.alianga.com/c/grep.html)

> global search regular expression and print out the line

文本搜索和筛选

```bash
 $ grep <patten> <file>                          # 从文件中筛选出符合模式的行, 可搜索多个文件
 $ egrep <regex> <file>                          # 与 grep -E 类似

 $ grep "3r" host.txt                            # grep 会显示所有包含 “3r” 的行
 > 3rd

 $ cat host.txt | grep "3r"                      # 与上述命令效果一致
 > 3rd

 $ grep -nE "[0-9]th" host.txt                   # 通过正则表达式匹配, 并显示行
 > 4:4th
 > 5:5th
 
 $ cat host.txt | egrep -i "[0-9]TH" | grep -v 5 # 多次管道筛选行
 > 4th                                           # 通过正则忽略大小写筛选, 去除包含 5 的行 
```

|parameter|meaning|
|:-:|:-:|
|`c`|`--count` 只显示匹配行的数量|
|`E`|`--extend-regexp` 使用正则匹配|
|`i`|`--ignore-case` 忽略大小写|
|`o`|`--only-matching` 只显示匹配到内容, 同行其它内容不显示|
|`n`|`--line-number` 同时显示行数|
|`v`|`--revert-match` 反转查找, 显示不匹配的所有行|
|`w`|`--word-regexp` 单词全匹配, 存在该单词的行, 不包含子字符串|
|`x`|`--line-regexp` 行全匹配, 必须与行完全一致 |

#### [wc](https://linux.alianga.com/c/wc.html) 

Word count 文字计数

```bash
 $ wc -c                                         # --bytes char 统计字符数量
 $ wc -w                                         # --words 统计单词数量
 $ wc -l                                         # --lines 统计行的数量

 $ cat host.txt | wc -l                          # wc 是以行尾是否有换行符号判断为一行
 > 4 host.txt                                    # 实际有 5 行, 第 5 行结尾没有换行符号
```

### 文本编辑

#### [xargs](https://linux.alianga.com/c/xargs.html) 

extended arguments: 文本格式转换与扩充

```bash
 $ <command> | xargs <options> <command>         # 处理左边命令的输出, 并作为右边命令的输入执行

 $ echo "end" | xargs echo "start"               # 将 "end" 传递给右边 echo 命令
 > start end                                     # 与 echo "start" "end" 一致
 
 $ cat host.txt | xargs -n 3                     # 读取文本内容, 修改格式, 每行 3 个字符串  
 > 1st 2nd 3rd                                   # xargs 右边不填命令, 默认使用 echo  
 > 4th 5th
 
 $ echo "1-2-3-4" | xagrs -d '-' -n 2            # 以 '-' 分割字符串, 分隔符号可以是单个字符,单个数字或单个字母 
 > 1 2                                           # 每行显示两个字符串
 > 3 4

 $ echo "1 2 3"| xargs -n 1 | xargs -i echo "line {} end"              
 > line 1 end                                    # xargs -n 1, 每行一个字符串, 将 1 行分割为 3 行
 > line 2 end                                    # -i 使用 {} 变量替换, 每一行内容替换掉 {} 执行
 > line 3 end

 $ cat host.txt | xargs -I num sh -c 'echo num start; echo num end' 
 > 1st start                                     # -I 设置变量 num(可自定义), 供后续多条命令执行 
 > 1st end                                       # 执行两次 echo 命令, num 替换为 cat 的输出
 > 2nd start
 > 2nd end
```

#### [sort](https://linux.alianga.com/c/sort.html)

文本行排序

```bash
 $ sort <file>                                   # 按每行第首字符的 ACSII 码值顺序排序, 相同则往后一个一个比较

 $ sort -r <file>                                # --reverse 反向排序
 $ sort -n <file>                                # 根据数值比较, 多位数看数值, 不再单个数字比较
 $ sort -u <file>                                # --unique 不显示重复的行
 $ sort -t : -k 2 -n <file>                      # 以 ':' 为分割符号, 第 2 个字符串按数字排序
```

#### [uniq](https://linux.alianga.com/c/uniq.html) : unique

```bash
 $ uniq <file>                                   # 合并相邻的重复行

 $ uniq -c                                       # --count 每行添加重复次数
 $ uniq -i                                       # --ignore-case 忽略大小写
 $ uniq -d                                       # --repeated 只显示重复行

 $ sort <file> | uniq -d                         # 先排序, 再打印相邻重复行, 显示文件所有重复行    
```

#### [tr](https://linux.alianga.com/c/tr.html) : transform

```bash
 $ tr <arg> <pattern>                            # 文本替换, 删除, 合并相邻重复

 $ tr ',' ' '                                    # 将 ',' 替换成空格
 $ tr 'A-Z' 'a-z'                                # 将大写替换成小写
 
 $ tr -d [0-9]                                   # 删除所有数字
 $ tr -s 'n'                                     # 合并所有重复 'n' 字符
```

注: tr 替换或删除时把字符集看做**多个字符**进行操作
如 tr -d 'abc' 表示删除文本中所有 a b c 字符

#### [sed](https://linux.alianga.com/c/sed.html) : stream editor

```bash
 $ sed <opt> <command> <file>

 $ sed -i <command> <file>                       # 逐行编辑文本内容 

 $ sed 's/<before>/<after>/' <file>              # s 替换指定字符(仅替换 1 次)
 $ sed 's/<before>/<after>/g' <file>             # g 替换指定字符(全替换)

 $ sed '/<regex>/d' file                         # 删除文件中符合正则的行
 $ sed '<num>d' file                             # 删除文件某一行, 可用 ',' 扩展范围 ('1,$d' 删除所有行)
```

#### [awk](https://linux.alianga.com/c/awk.html)

```bash
 $ awk 'BEGIN{cmds} <opt> {cmds} END{cmds}'      # {} 内填代码块, 中间是循环体,对每行执行
 
 $ awk '{print}' <file>                          # 逐行打印文件, BEGIN 和 END部分选填
 $ awk 'END{print NR}' <file>                    # NR 表示当前行号, 执行 END 时读完文件, NR 表示最后一行行号
 $ awk 'BEGIN{i=0} {i++} END{print i}' <file>    # BEGIN 时设置 i, 每一行 i 自加, 结束时打印

 $ awk '{print $5, $NF}' <file>                  # 以空格为分隔,打印第 5 及 最后一列
 $ awk -F ':' '{print $5, $NF}' <file>           # 以 ':' 为分隔,打印第 5 及 最后一列

 $ awk 'NR%2==0{print}' <file>                   # 过滤行, 只打印偶数行
 $ awk '/<regex>/' <file>                        # 只打印正则匹配的的行, 可用 '/<regex>/, /<regex>/' 打印区间
```

## 正则表达式