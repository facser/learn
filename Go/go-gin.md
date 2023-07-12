# Gin

[Gin官网](https://gin-gonic.com/zh-cn/)

Gin 是一个用 Go (Golang) 编写的 HTTP Web 框架

## 安装

使用 `go get -u` 下载最新的 gin 包, 同时把依赖信息写入 go.mod

```bash
 $ go env -w GOPROXY=https://goproxy.cn,direct   # 设置 go 下载源为国内源
 $ go get -u github.com/gin-gonic/gin            # 下载 Gin 依赖包
 
 $ go list -m all | grep gin
 > github.com/gin-gonic/gin v1.9.1
```

