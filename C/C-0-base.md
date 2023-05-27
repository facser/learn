# C

## 示例

创建 main.c 文件，写入代码

```c
#include <stdio.h>                               // 引入标准库 stdio.h (/usr/include/)

int main(void) {                                 // 定义执行入口, 入口函数名称固定为 main
    printf("hello world!");                      // 使用 stdio.h 中的 printf 函数
    return 0;
}
```

使用 GCC 编译

```bash
$ gcc main.c -o main                             # 编译 main.c 文件成可执行文件 main 
$ ./main                                         # 执行 main 
> hello world!                                   # 显示执行结果
```

C 是编译性语言, C 代码需要编译成可执行文件之后才能运行

```bash
main.c  --1--> main.i --2--> main.s --3--> main.o --4--> main

# main.c -> main.i 预处理, 展开头文件，宏替换，全掉注释，条件编译
# main.i -> main.s 编译 优化转化成汇编代码
# main.s -> main.o 汇编转成机器码
# main.o -> main   链接到一起生产可执行文件
```

## 格式

```c
int num;                                         // 声明变量 <类型> <变量名>; 分号是必须的
num = 1;                                         // 变量必须声明后才可以赋值

int num = 2;                                     // 变量声明并赋值, 等号两边空格不是必须

int                                              // 语句以分号结尾, 编译器会忽略换行
num
=
3;

```

```c
int add (int x, int y) {                         // <return type> <function name> (<arg type> <arg name>) {  
    int sum = x + y;                             // code block
    return sum;                                  // code block
}                                                // }  function end
```

## 关键字

```c
branch:    if     else  switch  case  default
loop:      for    do    while
jump:      break  goto  return  continue 

Functions: sizeof typedef 
Type:      void   int    char   float    double 
           union  enum   struct   
Modifiers: short  long   signed unsigned 
           const  static auto   register extern  volatile
```
