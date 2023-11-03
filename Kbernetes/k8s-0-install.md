<!--
 * @Author       : facsert
 * @Date         : 2023-10-30 09:59:08
 * @LastEditTime : 2023-10-30 10:08:18
 * @Description  : edit description
-->

# Kbernetes Install

## Install

安装 `minikube` 和 `kubectl`

[minikube 安装官网](https://minikube.sigs.k8s.io/docs/start/)

```bash
 $ uname -m                                      # 查看 CPU 架构
 > x86_64

 $ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 # x86-64 架构
 $ sudo install minikube-linux-amd64 /usr/local/bin/minikube


 $ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64 # arm64 架构
 $ sudo install minikube-linux-arm64 /usr/local/bin/minikube


 $ minikube start                                # root 用户添加参数 --force 
```