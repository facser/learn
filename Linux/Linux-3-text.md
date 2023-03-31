# Linux Text

## 文本搜索

### [grep](https://linux.alianga.com/c/grep.html) : global search regular expression and print out the line

```bash
 $ grep <patten> <file>                          # 从文件中筛选出符合模式的行, 可搜索多个文件

 $ grep -i                                       # --ignore-case 忽略大小写
 $ grep -E                                       # --extend-regexp 使用正则匹配

 $ grep -v                                       # --revert-match 显示不匹配的所有行
 $ grep -n                                       # --line-number 同时显示行数
 
 $ grep -c                                       # --count 只显示匹配行的数量
 $ grep -l                                       # 查询多个文件, 仅显示包含的文件名

 $ grep -w                                       # --word-regexp 单词全匹配, 存在该单词的行, 不包含子字符串
 $ grep -x                                       # --line-regexp 行全匹配, 必须与行完全一致 

 $ egrep <regex> <file>                          # 与 grep -E 类似
```

#### [cut](https://linux.alianga.com/c/cut.html) 

```bash
 $ cut <arg> <pattern> <file>                    # 截取指定列

 $ cut -f <num>                                  # 显示第 <num> 列, 以空格为分隔符, 从 1 开始
 $ cut -d <char>                                 # 自定义分隔符
 $ cut -c 3-6                                    # 显示每行第 3 至 6 个字符, 可填单个数字

 $ cut -d ':' -f 2,3                             # 根据 ':' 分割显示第 2, 3 列 
```

### 文本编辑

#### [xargs](https://linux.alianga.com/c/xargs.html) : extended arguments

```bash
 $ cat a.log | xargs                             # 多行内容输出单行 
 
 $ cat a.log | xargs -n 3                        # 重新修改格式, 每行 3 个字符串  
 $ cat a.log | xargs -d ,                        # 以 ',' 分割整行
 $ cat a.log | xargs -I {} touch {}              # {} 变量替换, 抓取文件每一行, 执行 touch line
```

#### [sort](https://linux.alianga.com/c/sort.html)

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

#### [wc](https://linux.alianga.com/c/wc.html) : Word count

```bash
 $ wc -c                                         # --bytes char 统计字符数量
 $ wc -w                                         # --words 统计单词数量
 $ wc -l                                         # --lines 统计行的数量
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