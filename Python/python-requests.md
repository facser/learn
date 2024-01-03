---
author: facsert
pubDatetime: 2023-12-13 20:57:56
title: Python requests
postSlug: ""
featured: false
draft: false
tags:
  - Python
  - requests
description: "Python HTTP 模块 requests"
---

<!--
 * @Author: facsert
 * @Date: 2023-12-13 20:57:56
 * @LastEditTime: 2023-12-13 20:58:57
 * @LastEditors: facsert
 * @Description:
-->

requests 是一个简单强大的 http请求库，支持同步和异步。

## 安装

```bash
 $ python -m pip install requests
 $ python -c "import requests" && echo $?
 > 0
```

## HTTP

`requests` 是一个 python 的 http 库, 它可以用来发送 http 请求, 并接收 http 响应  
HTTP 的全称是 HyperText Transfer Protocol (超文本传输协议)的缩写，是一种建立在 TCP 上的无状态连接  
HTTP 是互联网的基础协议，用于客户端与服务器之间的通信，它规定了客户端和服务器之间的通信格式，包括请求与响应的格式  

客户端通过地址链接生成 HTTP 报文, 并发送给服务器, 服务器根据请求方法，向客户端返回响应  

```bash
# 请求 URL
http://localhost:8001/node/get?id=1              

# HTTP 报文主要信息
Request URL: http://localhost:8001/node/get?id=1 # 请求 URL
Request Method: GET                              # 请求方法
Status Code: 200 OK                              # 响应状态码
Remote Address: 127.0.0.1:8001
Referrer Policy: strict-origin-when-cross-origin

# chrome General 请求报文所有信息
accept: application/json                         # 客户端接收的数据格式
Accept-Encoding: gzip, deflate, br               # 客户端接收的数据压缩格式
Accept-Language: zh-CN,zh;q=0.9                  # 客户端接收的语言                         
Cache-Control: no-cache  
Connection: keep-alive                           # 连接类型
Host: localhost:8001                             # 服务器地址
Pragma: no-cache
Referer: http://localhost:8001/
sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36

# HTTP 响应
content-length: 39                               # 响应数据长度
content-type: application/json                   # 响应数据格式
date: Wed, 03 Jan 2024 13:48:14 GMT              # 响应时间
server: uvicorn
```

## 发送请求

```python
import requests

# 发送 GET 请求
r = requests.get('http://localhost:8001/node/get?id=1')
print(r.status_code)
print(r.text)

# 发送 POST 请求
data = {'id': 1}
r = requests.post('http://localhost:8001/node/get', data=data)
```
