# Golang

[数组](#数组)
[切片](#切片)

## 数组

数组是**确定数量**元素的集合, 数组元素类型可以不一致
数组有容量和长度两个属性 `cap() len()` 查看数组属性
数组的长度和容量始终相等
数组元素可以修改, 但是数组长度和容量声明后就不能修改
数组中未赋值的元素会使用类型的默认值

```go
strList := [3]string{"hey", "you", "world"}      // 定义长度为 3 , 元素类型为字符串的数组
strList := [...]string{"hey", "you", "world"}    // 定义元素为字符串的数组, 根据值推断长度和容量

intList := [3]int{1, 2}                          // [1 2 0] 定义容量长度均为 3, 类型为 int 的数组
intList := [...]int{1, 2}                        // [1, 2]  容量和长度均为 2 的 int 数组

intArray := [3]int{1, 4}                         // [1 4 0] 初始化数组, 未定义的值取 0
intArray[1], intArray[2] = 2, 3                  // [1 2 3] 修改数组的值

len(strList)                                     // 3 strList 长度为 3
cap(intList)                                     // 3 intList 容量为 3
```

### any 类型数组

any 类型数组的元素可以是任意类型

```go
 var anyList [3]any                              // [<nil> <nil> <nil>] any 类型初始值是 nil
 anyList[0], anyList[1] = "he", 20000            // [he 2 <nil>]
 
 anyList[0] = anyList[0].(string) + " llo"       // any 转实际类型操作需要显示声明
 anyList[1] = anyList[1].(int) + 1
  
 for index, value := range anyList {
    fmt.Printf("index: %v, value: %v  type: %T\n", index, value, value)
 }

 > index: 0, value: hello type: string 
 > index: 1, value: 20000 type: int 
 > index: 2, value: <nil> type: <nil> 
```

### 数组值传递

不同长度的数组是不同类型
数组作为参数时需要确定数组长度

```go
 array := [...]int{0, 1, 2, 3}
 
 func (list [4]int) {                            // 数组作为参数时, 实参的长度和类型都必须和形参一致
     for i:= 0; i<= len(list); i++ { list[i] = i }
     fmt.Println(list)                           // [0 1 2 3] 传入函数的是数组的复制体, 不改变原先数组内容
 }(array)
 fmt.Println(array)                              // [0 0 0 0] 数组赋值和传参都会复制数组使用, 不改变原数组

 func (list *[4]int) {
     for i:= 0; i<= len(list); i++ { list[i] = i }
     fmt.Println(list)                           // &[0 1 2 3] 传入数组的地址, 修改地址对应的值相当于改变原数组
 }(&array)
 fmt.Println(array)                              // [0 1 2 3] 数组地址赋值和传参都会复制数组使用, 会改变原数组
```

## 切片

切片是一组**数量可变**的元素集合
切片是引用类型, 切片赋值传递的是地址
切片容量在切片不断追加元素后不断增长以存储所有添加的数据

```go
var strSlice []string                            // nil 切片声明, 创建一个 nil 切片, 与 nil 相等 
intSlice := []int{}                              // [] 切片声明并初始化, 创建空切片, 与 nil 不相等
boolSlice := make([]bool, 1, 2)                  // [false] 初始化布尔切片, 长度为 1, 容量为 2

fmt.Println(strSlice == nil)                     // true nil 切片与 nil 一致
fmt.Println(intSlice == nil)                     // false 空切片与 nil 不一致
```

### 切片特性

```go
intSlice := []int{0,0,0,0}                       // 整数切片初始化
intArray := intSlice                             // 切片赋值, 传递的是地址, 两切片指向同一个数组
            
intArray[0] = 1                                  // intArray 序号 0 重新赋值, intSlice 跟着变化
intArray = append(intArray, 2)                   // append 添加元素, 产生新的切片, intArray 变更指向的数组
intArray[1] = 1                                  // intArray 序号 1 重新赋值

fmt.Printf("intArray: %v intSlice: %v\n", intArray, intSlice)
> intArray: [1 1 0 0 2] intSlice: [1 0 0 0]      // 切片扩容后, 两切片指定数组不同，值互不影响
```

### 切片操作

`make` 构造切片

```go
make([]int, 3, 5)                                // [0 0 0] 构造长度 3 容量 3 的切片
```

切片使用 `append` 添加 删除 插入元素

```go
 slice := []int{0,0,0,0}
 slice = append(slice, []int{1, 1}...)           // append 添加数据 [0 0 0 0 1 1] 
 slice = append(slice[:1], slice[3:]...)         // append 删除数据 [0 0 1 1] 
 slice = append(slice[:1], append([]int{2}, slice[1:]...)...)

 fmt.Printf("slice: %v\n", slice)
 > slice: slice: [0 2 0 1 1]                     // append 插入数据

 slice := []int{4,1,6,2}
 fmt.Println(sort.Ints(slice))                   // 切片排序
 > [1 2 4 6]
```

截取切片片段 slice[low:high]
切片索引

```go
slice := []int{0,1,2,3}

slice[:2]
slice[1:]
slice[1:2]
slice[:]
```
