<!--
 * @Author       : facsert
 * @Date         : 2023-11-23 08:58:24
 * @LastEditTime : 2023-11-23 10:09:22
 * @Description  : edit description
-->

# loguru

## 介绍

loguru 是一个第三方记录日志的 Python 库, 可以简单快速配置日志记录.

```bash
 $ python -m pip install loguru
 $ pip list | grep loguru
 > loguru             0.7.2
```

```py
from loguru import logger

logger.info("this is a info log")
logger.error("this is a error log")
logger.debug("this is a debug log")

2023-11-23 09:04:56.748 | INFO     | __main__:<module>:10 - this is a info log
2023-11-23 09:04:56.749 | ERROR    | __main__:<module>:11 - this is a error log
2023-11-23 09:04:56.749 | DEBUG    | __main__:<module>:12 - this is a debug log
```

## 配置输出

默认输出包含多个内容和设定

```bash
level : `'DEBUG'`                                                              # 只显示 DEBUG 界别上的 log
format:  '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
  time : '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>'                       # 2023-11-23 09:04:56.749
  level: '<level>{level: <8}</level>'                                          # INFO     左对齐, 8 个字符, 空格补全
  model: '<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>'     # __main__:<module>:10 函数名, 行号
  msg  : '<level>{message}</level>'                                            # this is a info log 打印 log 
```

|Tag|TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Severity|5|10|20|25|30|40|50|
|methon|`trace`|`debug`|`info`|`success`|`warning`|`error`|`critical`|

默认输出内容比较冗余, 可以通过 `logger.remove()` 删除默认输出, 然后通过 `logger.add()` 重新配置输出.

```py
import sys
from loguru import logger

logger.remove()                                                                # 删除默认输出
fmt = '[<level>{level: <8}</level>][<green>{time:YYYY-MM-DD HH:mm:ss}</green>]: <level>{message}</level>'
logger.add(sys.stderr,  level='INFO', format=fmt)                              # 重新配置默认输出, level='INFO' 表示输出INFO级别以上的日志

logger.info("this is a info log")
logger.error("this is a error log")
logger.debug("this is a debug log")

[INFO    ][2023-11-23 09:12:40]: this is a info log
[ERROR   ][2023-11-23 09:12:40]: this is a error log
```

## 自定义输出

```py

···