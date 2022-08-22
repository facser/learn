# 代码设计和思考

如何写出高效优雅的代码？
如何设计代码逻辑？

---
写程序让机器看懂

用代码描述 人理解 的过程或对象

## 接口 API

(Application Programming Interface)

编程的本质: 调用 API 封装

控制
实现: 库 模块

描述模拟现实事物和队形
属性 行为

## 数据

## 函数

调用和封装

## 代码质量

### 可读性

- 代码是否容易阅读, 注释是否详细
- 代码嵌套较少, 较为简单
- 模块划分是否合理
  
### 可扩展性

- 是否预留扩展空间
- 代码复用性强
  
### 可维护性

- 是否易于修改 bug
- 是否易于添加或者修改代码
- 能应对多种异常

### 高效性

## 面向过程 OP

> Procedural-Oriented Programming

数据和算法分开

## 面向对象 OOP

> Object-oriented programming

简化程序的设计，我们引入了函数的概念，把相对独立且经常重复使用的代码放置到函数中，在需要使用这些功能的时候只要调用函数即可；如果一个函数的功能过于复杂和臃肿，我们又可以进一步将函数继续切分为子函数来降低函数的复杂性

序中的数据和操作数据的函数是一个逻辑上的整体，我们称之为“对象”

面向对象编程是一种开发理念, 与之相对的是面向过程

什么是对象
Everything is object (万物皆对象)

我们可以从两个层次来理解
对象是单个事物的抽象
对象是一个容器，封装了属性（property）和方法(method)
属性：对象的状态
方法：对象的行为
在实际开发中，对象是一个抽象的概念，可以将其简单理解为：数据集或功能集。
ECMAScript-262 把对象定义为：无序属性的集合，其属性可以包含基本值、对象或者函数。
什么是面向对象
面向对象编程 —— Object Oriented Programming，简称 OOP ，是一种编程开发思想。
它将真实世界各种复杂的关系，抽象为一个个对象，然后由对象之间的分工与合作，完成对真实世界的模拟。
面向对象与面向过程对比
面向过程就是亲力亲为，事无巨细，面面俱到，步步紧跟，有条不紊
面向对象就是找一个对象，指挥得结果
面向对象将执行者转变成指挥者
面向对象不是面向过程的替代，而是面向过程的封装

### 对象

#### 继承

#### 封装

#### 多态

## SOLID 原则

SOLID 是面向对象编程应当遵守的准则和最佳的实践方向

- SRP 单一职责
- OCP 开闭原则
- LSP 里式替换原则
- ISP 接口替换原则
- DIP 依赖倒置原则

### SRP 单一职责

#### 原始定义

> Single Responsibility Principle
> There should never be more than one reason for a class to change

译: 有且仅有一个原因引起类的变更, 简而言之, 一个类最好只负责一件事

SRP 原则在实际的重点在职责划分, 对于不同场景和需求来说, 职责的划分标准也不同.

### OCP 开闭原则

原始定义:
> Open Closed Principle

### LSP 里式替换原则

原始定义:
> Liskov Substitution Principle

### ISP 接口替换原则

原始定义:
> Interface Segregation Principle

### DIP 依赖倒置原则

原始定义:
> Dependency Inversion Principle

## 命名

### 介绍

创建一个自定义数据或者需要被复用的数据会对数据进行命名

### 命名方式

```bash
ErrorTestMessage            # 大驼峰 大小写混用区分逻辑断点
errTestMsg                  # 小驼峰

error_test_message          # 蛇形命名  
err_test_msg  
```

附录:[变量缩写](#变量缩写)



#### 命名内容

变量命名: 名词 形容词

- 描述变量的意义
- 要强调的描述放在最后
- 命名形式一致
  
布尔值常用前缀
|前缀|含义|
|:-:|:-:|
|is_xx|是不是|
|has_xx|有没有|
|should_xx|是否应该|
|can_xx|能不能|

强调的描述放后面

```python
xx_count      # xx 的数量
xx_length     # xx 的长度
xx_id         # xx 的 id
list_xx       # xx 列表
dict_xx       # xx 字典
int_xx        # xx 数字
```

函数: 动词 + 宾语

附录: [函数动词](#函数常用动词)

## 分支

### 提前结束

- 减少分支嵌套
- 用变量名对具体的值进行注释



### 边界问题

- LBYL:  Look Before You Leap
- EAFP: Easier to Ask for Forgiveness than Permission
  
```python
# 多分支嵌套, 多个条件成立后才执行
def get_list_index(value, lst):
    if instance(lst, list):
        if value in lst:
            return lst.index(value)
        else:
            print('value not in lst')
            return -2
    else:
        print('lst type error')
        return -1
 
# 提前结束, 不符合直接退出
def get_list_index(value, lst):
    type_err = -1 
    if not instance(lst, list):
        print('lst type error')
        return type_err 
        
    value_err = -2
    if  value not in lst:
        print('value not in lst')
        return value_err 
        
    return lst.index(value)

# 先使用, 报错了再解决
  def get_list_index(value, lst):
    try:
        return lst.index(value)
    except Exception as err:
        type_value_err = -1
        print(err)
        return type_value_err 
```

## 附录

### 变量缩写

```python
    addition              add               加
    subtraction           sub               减
    multiplication        mul               乘法
    division              div               除法
    hexadecimal           hex               十六进制
    array                 arr               数组、集合
    list/Sequence         lst/seq           列表 
    dictionary            dict              字典
    character             char              字符
    string                str               字符串
    text                  txt               文本
    number                num               数量、编号
    image                 img               图像
    length                len               长度
    summation             sum               和
    average               avg               平均
    maximum               max               最大值
    minimum               min               最小值
    middle                mid               中值
    source                src               源头
    address               addr              地址
    previous              pre               前一个
    current               cur               当前的
    initalize             init              初始化
    database              db                数据库
    administrator         adm               管理员
    password              pwd               密码
    user                  usr               用户
    directory             dir               目录
    document              doc               文档
    library               lib               库
    function              func              函数
    object                obj               对象
    argument              arg               实参
    variable              var               变量
    parameter             param             参数(形参)
    execute               exec              执行
    command               cmd               命令
    configuration         config            配置
```

### 函数常用动词

```python
    添加/插入                      add、append、insert、
    创建/初始化                    create、initialize、
    加载/选择                      load、pick、select
    删除/销毁                      delete、remove、destroy、drop
    打开/启动                      open、start
    关闭/停止                      close、stop
    获取/读取                      get、fetch、acquire、read、
    查找/查询                      search、find、query
    设置/重置                      set、reset
    放入/写入                      put、write、
    释放/刷新                      release、refresh
    发送/推送                      send、push
    接收/拉取                      receive、pull
    提交/取消                      submit、cancel
    收集/采集                      collect、
    提取/解析                      sub、extract、parse
    编码/解码                      encode、decode
    填充/压缩                      fill、pack、compress
    清空/解压                      flush、clear、unpack、decompress
    增加/减少                      increase、decrease、reduce
    分隔/拼接                      split、join、concat
    过滤/校验/检测                 filter、valid、check
```
