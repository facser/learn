# Golang

## Map

map 是一组**无序**的键值对的集合
map 是引用类型, 赋值时传递的是地址

```go
 map[<key type>]<value type>                     // map 类型

 var strMap = make(map[string]string, 1)         // 声明并初始化一个 empty map, map 容量为 2
 strMap["a"] = "a"                               // 已初始化的 map 赋值
 strMap["b"] = "b"

 intMap := map[string]int {                      // intMap 声明并初始化, 并赋值
     "one": 1,
     "two": 2,
 }

 Printf("int map %#v\n", intMap)
 Printf("str map %#v\n", strMap)
 Printf("str map length %v\n", len(strMap))

 > int map map[string]int{"one":1, "two":2}      
 > str map map[string]string{"a":"a", "b":"b"}   // map 可添加数据, 允许超过容量
 > str map length 3                              // 无法使用 cap 查看 map 容量, 可以使用 len 查看长度
```

```go
 intMap := map[string]int {
     "1st": 1,
 }
 
 copyMap := intMap                               // map 是引用类型, 传递的是引用并非数据的拷贝
 copyMap["2nd"] = 2                                                  
 intMap["1st"] = 4                               
 
 Printf("intMap %#v\n", intMap)
 Printf("copyMap %#v\n", copyMap)

 > intMap map[string]int{"1st":4, "2nd":2}       // 任意一个变量修改数据, 两个变量都会同步修改
 > copyMap map[string]int{"1st":4, "2nd":2}      // 两个变量指向同一个值, 结果一致
```

```go
 intMap := map[string]int {
    "1st": 1,
    "2nd": 2,
    "3rd": 3,
 } 

 for key, value := range intMap {
    Printf("%v: %v\n", key, value)
 }

 > 1st: 1
 > 2nd: 2
 > 3rd: 3
```

```go
 intMap := map[string]int {
    "1st": 1,
    "2nd": 2,
 } 

 value, ok := intMap["3rd"]                      // map 取值

 if ok == true {                                // ok 为 true, vaule 为对应 key 的值
    Printf("value: %v\n", value)
 }

 if ok == false {                                // ok 为 false, map 不存在 key, value 为类型零值
    Printf("key not in map")
 }
```

## Struct

```go

```
