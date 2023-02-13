# Golang


## 数组

数组是**确定数量**元素的集合, 元素类型可以不一致

```go
 strList := [3]string{"hey", "you", "world"}     // 定义长度为 3 , 元素为字符串的数组
 strList := [...]string{"hey", "you", "world"}   // 定义元素为字符串的数组, 根据值推断长度和容量

 intList := [3]int{1, 2}                         // [1 2 0] 定义容量长度均为 3, 类型为 int 的数组
 intList := [...]int{1, 2}                       // [1, 2]  容量和长度均为 2 的 int 数组

 intArray := [3]int{1, 4}                        // [1 4 0] 
 intArray[1], intArray[2] = 2, 3                 // [1 2 3]

// 数组有容量(cap())和长度(len())属性
// 数组中未定义元素会使用类型默认值, 数组容量和长度始终一致
// 数组中元素值可以修改, 但数组容量长度不能变
```

```go
 var anyList [3]any                              // [<nil> <nil> <nil>] any 类型初始值是 nil
 anyList[0], anyList[1] = "first", 2             // [first 2 <nil>]
 
 for index, value := range anyList {
    fmt.Printf("index: %v, value: %v\n", index, value)
 }

 > index: 0, value: first
 > index: 1, value: 2
 > index: 2, value: <nil>
```

```go
 
```

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

```go
 var strSlice []string                           // []
 intSlice := []int{1, 2}                         // [1 2]


```