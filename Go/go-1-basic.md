# Go

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
