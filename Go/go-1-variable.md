# Go

- [变量](#变量)
- [常量](#常量)
- [附录](#附录)

## 变量

- Go 变量命名要求以字母或下划线开头
- 不可以使用 Go 中的 25 [关键字](#关键字)及 37 个[保留字](#保留字)
- 变量要求声明类型使用类型推导

### 变量声明

```go
 var variable string                             // 声明变量和类型
 
 var age int = 18                                // 声明变量类型并赋值

 var age = 18                                    // 声明变量, 赋值, 并使用类型推导

 name := "facser"                                // 声明变量, 赋值, 并使用类型推导(仅限于函数内使用)
```

### 匿名变量

注: Go 中存在未被使用的变量会报错, 需要将其赋值给匿名变量 "_" 才能正常运行

```go
 var name string = "facser"
 fmt.Println("hellow world")

 > ./main.go:10:6: name declared but not used    // 变量 name 未使用, 报错

 name, _ := foo()                                // 使用匿名变量, 忽略 foo() 中一个返回值 
 fmt.Println("hellow ", name)

 > hellow  facser
```

## 常量

```go
 const e = 2.7182                                // 常量声明必须要赋值

 const (                                         // 快速声明常量, a b c 赋值 10
    a = 10
    b
    c
 )
```

### iota

```go
 const (
    a = iota                                     // 0
    b                                            // 1
    c                                            // 2
 )

 const (                                         // 变更初始值
    a = iota + 3                                 // 3 
    b                                            // 4
    c                                            // 5
 )

 const (                                         // iota 插值
    a = iota                                     // 1
    b = 5                                        // 5
    c = iota                                     // 2
    d                                            // 3
 )

```

## 打印

```go
 fmt.Println("Hello, world!")
 fmt.Print("number: %d", 4)

 fmt.Println("variable type: %T", <var>)
```

## 查看类型

```go
 reflect.TypeOf(<var>).Kind()
 reflect.TypeOf(<var>)
```

## 类型转换

```go
 strconv.Atoi()

 strconv.Itoa()
```

## 字符串操作

```go
 strings.Split(<str>, <split char>)              # 切割字符串成切片
 strings.Contains(<str>)                         # 判断是否包含
 strings.Index(<str>)                            # 字符串出现的位置
 strings.Join(<slice>, <join cahr>)              # 通过连接符号把切片连接成一个字符串
```

## 附录

### 关键字

```go
    break        default      func         interface    select
    case         defer        go           map          struct
    chan         else         goto         package      switch
    const        fallthrough  if           range        type
    continue     for          import       return       var
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