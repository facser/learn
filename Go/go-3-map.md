# Golang

## Map

map 是一组**无序**的键值对的集合
map 是引用类型, 赋值时传递的是地址

### map 初始化

map 只声明不初始化取零值 nil, nil map 只能读不能写入
map 初始化未添加值是 empty map, empty map 不等于 nil map

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

### map 传递

map 将引用拷贝了一份给赋值变量, 两个引用指向同一个数据
map 作为函数参数传递时也是拷贝一份引用进入函数

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

### map 遍历

map 使用 range 遍历 map
map 值拷贝也需要使用 range 遍历

```go
 intMap := map[string]int {
    "1st": 1,
    "2nd": 2,
    "3rd": 3,
 } 

 copyMap := make(map[string]int, 3)

 for key, value := range intMap {
    copyMap[key] = value
    Printf("%v: %v\n", key, value)
 }

 > 1st: 1
 > 2nd: 2
 > 3rd: 3
```

### map 取值

```go
 intMap := map[string]int {
    "1st": 1,
    "2nd": 2,
 } 

 value, ok := intMap["3rd"]                      // map 取值

 if ok == true {                                 // ok 为 true, vaule 为对应 key 的值
    Printf("value: %v\n", value)
 }

 if ok == false {                                // ok 为 false, map 不存在 key, value 为类型零值
    Printf("key not in map")
 }
```

### map 删除

```go
 intMap := map[string]int{
    "1st": 1,
    "2nd": 2,
 }

 delete(intMap, "1st")
```

## Struct

### struct 初始化

```go
 type <struct name> struct {                     // 定义结构体, 结构体可以认为是自定义的数据类型
   <attribute name>  <type>                      // 定义结构体属性及其类型
   <attribute name>  <type>                      // 每个属性名唯一, 不能重复
   ...
 }

 type Student struct {                           // 定义 Student 类型数据
   name, city  string                            // Student 类型有 name city 属性, 属性值为 string
   age int                                       // Student 类型有 age 属性, 属性类型为 int
 }

 var kertory Student                             // 初始化 Student 类型变量 kertory
 kertory.name = "kertory"                        // 使用 . 赋值
 kertory.age = 18

 facsert := Student{                             // 初始化 Student 类型变量 facsert
   name: "facsert",
   city: "shanghai",
 }

 Printf("%#v\n", kertory)
 Printf("%#v\n", facsert)

 > main.Student{name:"kertory", city:"", age:18} // 未初始化的属性使用类型的零值 
 > main.Student{name:"facsert", city:"shanghai", age:0}
```

### struct 方法

```go
 type Student struct {
   name, city string
   age int
 }

 func (s Student) Learn() {
   Printf("%s learnig in %s\n", s.name, s.city)
 }

 func (s Student) Play() {
   Printf("%s play games\n", s.name)
 }

 facsert := Student{
    name: "facsert",
    city: "shanghai",
 }

 facsert.Learn()
 facsert.Play()

 > facsert learnig in shanghai
 > facsert play games
```

### struct 属性修改

```go
 type Student struct {
   name, city string
   age int
 }

 func (s Student) rename1(name string) {         // 重命名属性 name
   s.name = name
   Printf("rename1 to %s\n", s.name)
 }

 func (s *Student) rename2(name string) {        // 重命名属性 name
   s.name = name
   Printf("rename2 to %s\n", s.name)
 }

 facsert := Student{
    name: "facsert",
    city: "shanghai",
 }

 facsert.rename1("kertory")
 facsert.rename2("squtary")
 Printf("name: %s\n", facsert.name)

 > rename1 to kertory                            // 重命名结果只在函数内生效
 > rename2 to squtary                            // 重命名结果对结构体生效
 > name: squtary
```

### struct 转 json

```go
import (
   . "fmt"
   "encoding/json"
)

 type Student struct {
     Name string                                 // 属性名大写其它模块可访问, 可以转 json
     city string                                 // 属性名小写其它模块不能访问也不能转 json
     Age int     `json:"age"`                    // 可以通过定义 tag, 修改转化为 json 后 key 名称 
}

 facsert := Student{
    Name: "facsert", 
    city: "shanghai",
    Age: 18,
 }

 jsonStu, err := json.Marshal(facsert)           // struct 转 json 
 if err != nil {
   panic("json mashal failed")
 }

 Println(facsert)
 Println(string(jsonStu))

 > {facsert shanghai 18}                         // facsert 结构体所有属性值
 > {"Name":"facsert","age":18}                   // city 属性不在, Age 属性名变为 age
```
