
# 代码风格

- 命名
- 注释
- 审美

## 命名

目标: 把值的信息放入名字里

- 准确
- 突出重点
- 一致
- 长度

### 准确

使用 **准确** **具体** **单一**的词

变量命名 名词 形容词
函数 动词 名词

[常用动词](#常用动词)

### 突出重点

通过 前缀 后缀 突出重点

|前缀|含义|
|:-:|:-:|
|is_xx|是不是|
|has_xx|有没有|
|should_xx|是否应该|
|can_xx|能不能|

避免反义命名

```python
 test_pass = True                                # 推荐 True 一般与成功, 正常对应 
 test_fail = False                               # 不推荐 False 一般与错误, 失败对应
```

度量命名带上单位

```python
 time_secs = 8
 time_hours = 2
 time_days = 3 
```

### 一致

### 长度

在小的作用区域内可以使用简短的变量名

使用常用的单词缩写

[常见单词缩写](#单词缩写)

## 注释

注释

## 审美

- 使用一致的布局
- 代码分组, 形成代码块

# 附录

## 常用动词

```shell
    添加/插入                      add, append, insert, 
    创建/初始化                    create, initialize, 
    加载/选择                      load, pick, select
    删除/销毁                      delete, remove, destroy, drop
    打开/启动                      open, start
    关闭/停止                      close, stop
    获取/读取                      get, fetch, acquire, read, 
    查找/查询                      search, find, query
    设置/重置                      set, reset
    放入/写入                      put, write, 
    释放/刷新                      release, refresh
    发送/推送                      send, push
    接收/拉取                      receive, pull
    提交/取消                      submit, cancel
    收集/采集                      collect, 
    提取/解析                      sub, extract, parse
    编码/解码                      encode, decode
    填充/压缩                      fill, pack, compress
    清空/解压                      flush, clear, unpack, decompress
    增加/减少                      increase, decrease, reduce
    分隔/拼接                      split, join, concat
    过滤/校验/检测                 filter, valid, check
```

## 单词缩写

```shell
    addition              add               加
    subtraction           sub               减
    multiplication        mul               乘法
    division              div               除法
    hexadecimal           hex               十六进制
    array                 arr               数组, 集合
    list/Sequence         lst/seq           列表 
    dictionary            dict              字典
    character             char              字符
    string                str               字符串
    text                  txt               文本
    number                num               数量, 编号
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
