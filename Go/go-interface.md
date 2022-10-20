# Go interface

接口是一个自定义类型, 类型判定较普通类型宽松很多, 对应变量或结构体只要实现了接口的方法就符合

type 歌唱家 interface {
    发声()
}

根据以上接口, 不管任何人甚至动物机器人, 只要能发出声音, 该个体就可以被认为是 歌唱家 类型
接口类型和其余 int string 一样可以作为类型声明
当参数被当做接口类型使用, 就无法使用接口之外的方法.

```go
type singer interface {                          // 定义 singer 接口类型
    sing()                                       // 该类型必须包含 sing 和 speak 方法
    speak()
}

func talk(item singer) {                         // 定义一个函数, 参数类型为 singer, 只要某个结构体包含 sing speak 函数, 就可以当参数
    item.sing()                                  // 传入的参数只能使用 singer 包含的方法, 参数本身的其它发放不能使用
    item.speak()
}

type person struct {                             // 定义 person 结构体
    name str
}

func (p person) sing() {                         // 定义结构体方法 sing 
    fmt.Println("lalala")
}
 
func (p person) speak() {                        // 定义结构体方法 speak
    fmt.Println("ok ok")
}


p := person{name: "facser"}                      // 实例化 person 结构体
talk(p)                                          // 因为实例 p 包含 sing speak 方法, 所以 p 可以作为 singer 类型使用

var s singer = person{name: "facser"}           // person 实例化后包含 sing speak, 可以作为 singer 类型
s.sing()
s.speak()
```