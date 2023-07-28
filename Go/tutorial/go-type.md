<!--
 * @Author       : facsert
 * @Date         : 2023-07-10 14:24:30
 * @LastEditTime : 2023-07-28 11:42:26
 * @Description  : edit description
-->

# Type

## 类型约束

```go
func detail[T string| int| bool](item T) {       // 多类型参数定义
    fmt.Printf("value: %v \n", variable)         // 打印变量的值
    fmt.Printf("type: %T", variable)             // 打印变量的类型
}

func add[T string| int](a T, b T) {              // 多类型参数定义, a b 类型相同, 且都为 string 或 int
    fmt.Println(a + b)                           // 打印结果
}
```
