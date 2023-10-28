<!--
 * @Author       : facsert
 * @Date         : 2023-10-28 14:52:02
 * @LastEditTime : 2023-10-28 15:29:34
 * @Description  : edit description
-->

# fastapi

## 介绍

## 安装

```bash
 $ python -m pip install "fastapi[all]"
 
 $ python -c "import fastapi"; echo $?
 > 0
```

```py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],                       # 允许所有源的请求
      allow_credentials=True,
      allow_methods=["*"],                       # 允许所有请求方法
      allow_headers=["*"],                       # 允许所有请求头
  )

@app.get("/")
async def root():
    return "root page"

if __name__ == "__main__":
    uvicorn.run(
        "main:app",                               # 启动文件
        host="0.0.0.0",                          # 绑定IP
        port=8000,                               # 绑定端口
        reload=True                     ,        # 自动重新加载
    )
```

浏览器打开   `http://0.0.0.0:8000/`  
swagger-ui  `http://0.0.0.0:8000/docs/`

## swagger-ui

[Github swagger-ui](https://github.com/swagger-api/swagger-ui.git)

打开 swagger 页面需要加载外界 CDN 资源，可能会非常慢，建议使用离线 swagger-ui 文件  
在 Github 下载官方 swagger-ui 资源, 放入项目 `static` 路径下, 在代码中配置即可  

```bash
project
├─ static
│  └──swagger-ui
│     ├── ...
│     └── README.md
└── main.py
```

```py
import uvicorn
from fastapi import FastAPI
from os.path import join, dirname
from os import getcwd
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.mount(
    join(getcwd(), 'static'), 
    name="static"
    StaticFiles(directory=join(getcwd(), 'static/swagger-ui'))
)

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  
      allow_credentials=True,
      allow_methods=["*"],  
      allow_headers=["*"],  
  )

@app.get("/")
async def root():
    return "root page"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```