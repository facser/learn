# Pointer

## 指针

变量

- 变量名
- 变量值
- 保存的地址

指针变量

- 变量名
- 变量值(值保存的是地址)
- 保存的地址

定义变量后, 该变量的地址不变, 地址内的值可变化

### 变量地址

- & 获取变量的地址
- * 指针变量取值

```go
 var str string = "hello"                        // 定义一个字符串变量 str, 值是 "hello" 地址是 0xc00001a078

 addr := &str                                    // addr 类型为 *string(地址类型), addr 的值是 0xc00001a078(str 地址), addr 地址是 0xc00000e018

 tmp := *addr                                    // 根据 addr 的值(0xc00001a078 str 地址)取值到 "hello" 赋值给 tmp. 等同于 tmp := "hello"
 
 *addr = "end"                                   // str 的地址不变, addr 指针一直指向 str 的值, 与 str = "end" 效果一致
```



