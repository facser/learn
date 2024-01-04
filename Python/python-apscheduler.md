---
author: facsert
pubDatetime: 2023-12-13 21:51:08
title: Python APScheduler
postSlug: ""
featured: false
draft: false
tags:
  - Python
  - APScheduler
description: "Python 定时任务框架 APScheduler"
---

<!--
 * @Author: facsert
 * @Date: 2023-12-13 21:51:08
 * @LastEditTime: 2023-12-13 22:10:40
 * @LastEditors: facsert
 * @Description:
-->

APScheduler 是一个 Python 定时任务框架, 支持 Cron、Interval、Date、Timeout 等类型的任务,  
支持分布式任务, 支持任务失败重试, 支持任务并发限制, 支持任务状态监控, 支持任务日志记录

## 安装与介绍

```shell
 $ pip install apscheduler
 $ python -c "import apscheduler" && echo "Installed"
 > Installed
```

apscheduler 有四个基本对象

scheduler: 调度器, 用于调度任务
job: 任务, 定义了任务执行的内容  
trigger: 触发器, 用于定义任务执行的规则  
executor: 执行器, 用于执行任务

## 基本使用

四种调度器:  
BlockingScheduler: 阻塞调度器, 适用于单线程的应用  
BackgroundScheduler: 后台调度, 不影响主线程  
AsyncIOScheduler: 异步IO调度器, 适用于多线程的应用  
GeventScheduler: gevent 调度器, 适用于多线程的应用  

三种触发器:  
cron: 基于 Cron 表达式的触发(周期性)  
interval: 固定间隔触发  
date: 基于日期, 特定时间只触发一次  

```py

def func(name='Jhon'):
    print(f'Hello, world!, {name}')

schedule = schedulers()                          # 选择一种调度器
schedule.add_job(func, 'interval', seconds=5)    # 每 5s 执行一次
scheculer.add_job(func, 'cron', minute='*/5')    # 每 5 分钟执行一次


date = '2024-01-04 12:00:00'                     # 固定时间执行一次
schedule.add_job(func, 'date', run_date=date, args=['lily'])

```

add_job() 方法的参数:  
func: 任务函数  
trigger: 触发器  
args: 任务函数的参数  
kwargs: 任务函数的参数  
id: 任务的唯一标识符  
name: 任务的名称  
misfire_grace_time: 任务失败重试时间  
coalesce: 是否允许任务重复执行  

```python
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor

def job_func():
    print('Hello, world!')

scheduler = BlockingScheduler()
scheduler.add_job(job_func, CronTrigger(second='*/5'))
```
