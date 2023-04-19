# Golang

[数组](#数组)
[切片](#切片)

## 数组

数组是**确定数量**元素的集合, 数组元素类型可以不一致

```go
strList := [3]string{"hey", "you", "world"}      // 定义长度为 3 , 元素为字符串的数组
strList := [...]string{"hey", "you", "world"}    // 定义元素为字符串的数组, 根据值推断长度和容量

intList := [3]int{1, 2}                          // [1 2 0] 定义容量长度均为 3, 类型为 int 的数组
intList := [...]int{1, 2}                        // [1, 2]  容量和长度均为 2 的 int 数组

intArray := [3]int{1, 4}                         // [1 4 0] 初始化数组, 未定义的值取 0
intArray[1], intArray[2] = 2, 3                  // [1 2 3] 修改数组的值

// 数组有容量(cap())和长度(len())属性
// 数组中未定义元素会使用类型默认值, 数组容量和长度始终一致
// 数组中元素值可以修改, 但数组容量长度不能变
```

### any 类型数组

```go
 var anyList [3]any                           // [<nil> <nil> <nil>] any 类型初始值是 nil
 anyList[0], anyList[1] = "he", 20000         // [he 2 <nil>]
 
 anyList[0] = anyList[0].(string) + " llo"     // any 转实际类型操作需要显示声明
 anyList[1] = anyList[1].(int) + 1
  
 for index, value := range anyList {
    fmt.Printf("index: %v, value: %v  type: %T\n", index, value, value)
 }

 > index: 0, value: hello type: string 
 > index: 1, value: 20000 type: int 
 > index: 2, value: <nil> type: <nil> 
```

### 数组值传递

```go
 array := [...]int{0, 1, 2, 3}
 
 func (list [4]int) {                            // 数组作为参数时, 参数类型必须带上容量
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

```go
 var strSlice []string                           // [] 字符串切片声明, 仅声明会创建一个 nil 切片 
 intSlice := []int{}                             // [] 整形切片声明并初始化, 初始化未赋值创建空切片
 boolSlice := make([]bool, 1, 2)                 // [false] 初始化布尔切片, 长度为 1, 容量为 2

 fmt.Println(strSlice == nil)                    // true nil 切片与 nil 一致
 fmt.Println(intSlice == nil)                    // false 空切片与 nil 不一致
 fmt.Println(boolSlice == nil)                   // false 切片之间无法直接比较
 
// 切片容量随着数据增长而增长
// 包含长度 len(slice), 容量 cap(slice) 属性
```

### 切片特性

```go
 intSlice := []int{0,0,0,0}                      // 整数切片初始化
 intArray := intSlice                            // 切片赋值, 传递的是地址, 两切片指向同一个数组
               
 intArray[0] = 1                                 // intArray 序号 0 重新赋值, intSlice 跟着变化
 intArray = append(intArray, 2)                  // intArray 添加元素, 切片指向新的数组
 intArray[1] = 1                                 // intArray 序号 1 重新赋值, 与 intSlice 指向数组不一致
 fmt.Printf("intArray: %v intSlice: %v\n", intArray, intSlice)

 > intArray: [1 1 0 0 2] intSlice: [1 0 0 0]     // 切片扩容后, 两切片指定数组不同，值互不影响
```

### 切片操作

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
