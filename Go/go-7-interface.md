# Golang interface

接口是一个自定义的抽象类型
接口用于定义函数的参数类型, 任意参数满足接口条件即可作为函数参数使用

```go
type <interface name> interface {
    <function name>(<parameter name> <parameter type>) <return type>
}

type app interface {                             // 定义一个 app 类型接口
    open(click int) string                       // 定义 app 类型需要满足的条件
    close(action string) string                  // 任意结构体实现了接口定义的方法就可以作为 app 类型使用
}

type browser struct (                            // 定义 browser 类型结构体
    name string                                  // 定义 browser 结构体属性
)

func (b browser) open(click int) string {        // browser 类型结构体实现 open 方法
    return Sprintf("click %d open %s", click, b.name)
}

func (b browser) close(action string) string {   // browser 类型结构体实现 close 方法
    return Sprintf("use %s close %s", action, b.name)
}

func relax(application app) {                    // 定义函数 relax, 函数参数为 app 接口类型
    Println(application.open(2))                 // 执行 read 方法
    Println(application.close("swipe up"))       // 执行 search 方法
}

chrome := browser{name: "chrome browser"}        // 实例化 chrome, chrome 包含 open close 方法
relax(chrome)                                    // chrome 满足接口条件, chrome 可以当做 app 类型使用
> click 2 open chrome browser
> use swipe up close chrome browser
```
