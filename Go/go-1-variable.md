# Golang  

- [变量](#变量)
- [常量](#常量)
- [打印](#打印)
- [整形](#整形)
- [字符串](#字符串)
- [附录](#附录)

## 变量

- Go 变量命名要求以字母或下划线开头
- 不可以使用 Go 中的 25 [关键字](#关键字)及 37 个[保留字](#保留字)
- 变量要求声明类型使用类型推导

### 变量声明

```go

 var <variable name> <type> = <value>            // 变量定义, 最完整的变量定义
 var age int = 18                                // 声明变量类型并赋值

 var <variable name> <type>                      // 变量定义, 只定义变量名和类型, 变量默认为对应类型的初始值
 var str string                                  // 声明变量和类型, 未赋值使用默认值(string 默认值 "")

 var <type> = <value>                            // 变量定义, 通过值自动推导变量类型
 var age = 18                                    // 声明变量, 赋值, 并使用类型推导

 <variable name> := <value>                      // 变量定义, 通过值自动推导类型, 仅能在函数内部使用
 name := "str"                                   // 声明变量, 赋值, 并使用类型推导(仅限于函数内使用)

```

### 匿名变量

注: Go 中存在**未被使用**的变量会报错, 需要将其赋值给匿名变量 "_" 才能正常运行

```go
 var name string = "facser"
 fmt.Println("hello world")
 > ./main.go:10:6: name declared but not used    // 变量 name 未使用, 报错

 name, _ := "facser", "variable"                 // 使用匿名变量, 忽略 foo() 中一个返回值 
 fmt.Println("hello ", name)
 > hello  facser
```

## 常量

```go
 const e = 2.7182                                // 常量声明必须要赋值, 且不可更改

 const (                                         // 快速声明常量, a b c 赋值 10
    a = 10                                       // a = 10
    b                                            // a = 10
    c = 5                                        // a = 5
    d                                            // a = 5
 )
```

### iota

iota 是定义常量时使用的自增关键字

不同 const 定义块互不干扰
所有注释行和空行全部忽略
从第 1 行开始，iota 从 0 逐行加 1

```go
 const (
    a = iota                                     // iota = 0  a = 0
    b                                            // iota = 1  b = 1
    c                                            // iota = 2  c = 2
 )

 const (                                         // 变更初始值
    a = iota + 3                                 // iota = 0  a = 3
    b                                            // iota = 1  b = 4
    c = iota + 2                                 // iota = 2  c = 4
    d                                            // iota = 3  d = 5
 )

 const (                                         // iota 插值
    a = iota                                     // iota = 0  a = 0
    b = 5                                        // iota = 1  b = 5
    c = iota                                     // iota = 2  c = 2
    d                                            // iota = 3  d = 3
 )

```

## 打印

通过占位符替换值打印

```go
 fmt.Printf(<str>, <string>, <int>, <bool> ...)  // 第一个参数是字符串,后接任意类型值, 占位符需与值数量对应 

 fmt.Printf("common: %v \n", "common")           // 万能占用符, 自动判断类型
 fmt.Printf("string: %s \n", "string")           // 字符串变量占位符
 fmt.Printf("char  : %c \n", 'c')                // 单个字符变量占位符, 单个字符用单引号
 fmt.Printf("number: %d \n", 4)                  // 整形变量占位符 
 fmt.Printf("float : %f \n", 2.33)               // 浮点型变量占位符
 fmt.Printf("bool  : %t \n", true)               // 布尔值变量占位符
 fmt.Printf("point : %p \n", *variable)          // 指针变量占位符

 fmt.Printf("variable type: %T \n", variable)    // 变量类型占位符
```

## 整形

|类型|范围|
|:-|:-|
|`int8`  |-128 - 127|
|`uint8` / `byte` |0 - 255|
|`int16` |-32768 - 32767|
|`uint16`|0 - 65535|
|`int32` / `rune` |-2147483648 ~ 2147483647|
|`uint32`|0 ~ 4294967295|
|`int64` |-9223372036854775808 ~ 9223372036854775807|
|`uint64`|0 ~ 18446744073709551615|
|`int`   |32 位系统 int32， 64 位系统 int64|
|`uint`  |32 位系统 uint32， 64 位系统 uint64|

### 整形类型转换

数字类型数据可以通过 `<type>()` 方式进行类型之间的转换

```go
 var num int = 8                                 // int   num = 8
 num8 := int8(num)                               // int8  num8 = 8
 num16 := int16(num)                             // int16 num16 = 8
 num32 := int32(num)                             // int32 num32 = 8
 num64 := int64(num)                             // int64 num64 = 8

 numFloat32 := float32(num)                      // float32 numFloat32 = 8
 numFloat64 := float32(num)                      // float64 numFloat64 = 8
```

### 进制赋值

```go
 binary := 0b11                                  // int binary      = 3   2 进制赋值 
 octal := 0o11                                   // int octal       = 9   8 进制赋值 
 hexadecimal := 0x11                             // int hexadecimal = 17  16 进制赋值 
```

## 字符串

Golang 字符串本质是单个字符的集合, 单个字符的本质是数字, 通过不同规范和字符对应(ACSII 和 Unicode)

byte(uint8) ACSII 表中的一个字符, 底层是一个 0-255 数字(数字与 ACSII 表字符绑定)
rune(int32) Unicode 编码中的一个字符(包含世界大部分语言字符), Unicode 表包含 ACSII 表

```go
 var a byte = 'D'                                 // 'D' 在 ACSII 中第 68 位
 var c byte = 68                                  // ACSII 中 68 为 'D', 两种赋值等价

 var a rune = '中'                                // '中' 在 Unicode 中第 20013 位
 var c rune = 20013                               // Unicode 中 20013 为 '中', 两种赋值等价
 
 fmt.Printf("a equal c: %v\n", a == c)
 > a equal c: true
```

```go
 var acsii, unicode string = "str", "中文"
 for _, char := range acsii {
     fmt.Printf("Type: %T, value: %v, value: %c\n", char, char, char)
 }
 
 > Type: int32, value: 115, value: s
 > Type: int32, value: 116, value: t
 > Type: int32, value: 114, value: r
 > Type: int32, value: 20013, value: 中
 > Type: int32, value: 25991,, value: 文

// 遍历字符串, 单个字符类型为 int32(rune)
// 默认使用 unicode 规范, 字符底层是数字, 与 Unicode 字符关联
```

```go
 slice, list := []byte("str"), []rune("中文")
 fmt.Printf("Type: %T, value: %v\n", slice, slice)
 > Type: []uint8, value: []byte{0x73, 0x74, 0x72}// 字符串转 byte
 > Type: []int32, value: []int32{20013, 25991}   // 字符串转 rune

 var strByte byte = 'D'
 var strRune rune = '文'
 fmt.Printf("Type: %T, value: %v\n", string(strByte), string(strByte))
 fmt.Printf("Type: %T, value: %v\n", string(strRune), string(strRune))
 > Type: string, value: D                        // byte 转 string
 > Type: string, value: 文                       // rune 转 string
```

```go
 var num int = 68
 var num8 int8 = 66
 var num16 int16 = 66
 var num32 int32 = 25991
 var num64 int64 = -1
 fmt.Printf("Type %T, value: %v\n", num, string(num))

 > Type int, value: D                            
 > Type int8, value: B
 > Type int16, value: B
 > Type int32, value: 文                          // 任意 unicode 范围内非负数可以通过内置函数 string() 转换为对应字符
 > Type int64, value: �                          // 所有负数转化后显示一致, 未能查询到相关解释

```

### 字符串操作

字符串定义后可以查看但不可更改

```go
 str := "learning"
 fmt.Printf("Type: %T value: %c golang: %v\n", str[0], str[1], str[2])
 > Type: uint8 value: e golang: 97

 str[0] = "m"
 > ./main.go:37:2: cannot assign to str[0] (value of type byte)

 uStr := "中文"
 fmt.Printf("Type: %T value: %v length: %v\n", uStr[0], uStr[1], len(uStr))
 > Type: uint8 value: 184 length: 6

 strRune := []rune(uStr)
 fmt.Printf("value: %#v length: %v\n", strRune, len([]rune(strRune)))
 > value: []int32{20013, 25991} length: 2

 // 单个英文字母 1 个 byte可以表示, len() 返回字节数, 一个字母占用 1 个字节
 // 单个中文字符由 3 个 byte 或 1 个 rune 表示, len() 返回字节数, 一个字符包含 3 个字节
 // 以 byte 区分, 单个中文字符长度为 3, 单个字母长度为 1
 // 通过序号取的单个字符为 byte(str[index]), 通过 range 取出的单个字符为 rune(for _, s := range str)
```

```go
 strings.Split(s, sep) []string                  // 以 sep 为分隔符, 切割字符串成切片
 strings.Contains(s, sub) bool                   // 判断 s 是否包含 sub
 strings.Index(s, sub) int                       // sub 在 s 的序号
 strings.Join(slice, sep) string                 // 通过 sep 把 slice 连接成一个字符串
 strings.Replace(s, old, new, count) string      // 将 s 中的 old 替换为 new, 替换 count 次
 strings.Count(s, sub) int                       // 返回 sub 在 s 中出现次数
```

## 布尔值

布尔值: true, false

```go
 love, happy := true, false
 
 !love                                           // false  not love is false
 love == happy                                   // false  love equal happy is false 
 love != happy                                   // true   love not equal happy
 happy && love                                   // false  love and happy is not true
 happy || love                                   // true   love or happy is true 
```

布尔类型的值默认值是 false
布尔值无法参数数值运算, 只能进行逻辑运算
布尔值只能转换为字符串, 无法转换为其它类型

## 类型转换

任意类型数据都可以转换为字符串

```go
s := fmt.Sprinf("%v", <variable>)                // 万能转换, any -> string

s := strconv.Itoa(32)                            // int -> string
s := strconv.FormatBool(true)                    // bool -> string
s := strconv.FormatFloat(3.1415, 'E', -1, 64)    // float64 -> string
s := strconv.FormatInt(-42, 16)                  // int64 -> string
s := strconv.FormatUint(42, 16)                  // uint63 -> string
```

字符串转其它类型可能会失败, 转数字时还需考虑进制和类型

```go
 i, err := strconv.Atoi("-42")                   // string -> int
 b, err := strconv.ParseBool("true")             // string -> bool
 f, err := strconv.ParseFloat("3.1415", 64)      // string -> float64
 i, err := strconv.ParseInt("-42", 10, 64)       // string -> int64
 u, err := strconv.ParseUint("42", 10, 32)       // string -> uint32

// ParseFloat (str, bitSize)  bitSize:{32:float32, 64:float64}

// ParseInt  ParseUint (str, base, bitSize)
// str string: 待转换的字符串
// base int: str 的进制( base=16, s 为 16 进制的字符串)
// bitSize int: {0:int, 8:int8, 16:int16, 32:int32, 64:int64}
```

## 附录

### 关键字

```go
   break        default      func         interface    select
   case         defer        go           map          struct
   chan         else         goto         package      switch
   const        fallthrough  if           range        type
   continue     for          import       retrun       var
```

### 保留字

```go
    Constants:    true  false  iota  nil

        Types:    int  int8  int16  int32  int64  
                  uint  uint8  uint16  uint32  uint64  uintptr
                  float32  float64  complex128  complex64
                  bool  byte  rune  string  error

    Functions:   make  len  cap  new  append  copy  close  delete
                 complex  real  imag
                 panic  recover

```
