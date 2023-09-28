<!--
 * @Author: facsert
 * @Date: 2023-09-27 21:03:53
 * @LastEditTime: 2023-09-28 21:13:24
 * @LastEditors: facsert
 * @Description: 
-->
# conda

Anaconda 是一个 python 版本管理器, 能快速创建虚拟环境, 管理 python 版本,安装包等.

## 安装

[Anaconda 官网](https://www.anaconda.com/) 下载对应平台安装包

## 常用命令

```bash
 $ conda info                                              # 查看 anaconda 基本信息
 $ conda --version                                         # 查看 conda 版本
 > conda 22.9.0

 $ conda env list                                          # 列出当前所有环境
 $ conda info -e                                           # 列出当前所有环境
 > # conda environments:
 > #
 > base                  *  /root/anaconda3                # 带 * 表示当前使用环境
 > py3.9                    /root/anaconda3/envs/py3.9     # 已创建环境

 $ conda update -n base -c defaults conda                  # 更新 conda 版本
 $ conda update -n base conda
```

## 创建环境

```bash
 $ conda create -n <name> python=<version>                 # 选择 python 版本创建虚拟环境并命名

 $ conda create -n py3.7 python=3.7                        # 创建 python 3.7 虚拟环境
 > Collecting package metadata (current_repodata.json): done
 > Solving environment: done
 > ......                                                  # 下载python版本包
 > Retrieving notices: ...working... done
```

## 启用退出

```bash
 $ conda activate <name>                                   # 激活指定环境
 $ conda activate py3.7                                    # 激活虚拟环境

 $ conda deactivate                                        # 退出当前环境

 $ conda rename -n <old name> <new name>                   # 重命名环境
 $ conda rename -n py3.9 py39
 > Source:      /root/anaconda3/envs/py3.9
 > Destination: /root/anaconda3/envs/py39
 > Packages: 21
 > Files: 926
 > Preparing transaction: done
 > Verifying transaction: done
 > Executing transaction: done
```

## 删除环境

```bash
 $ conda env remove -n <name>                               # 删除指定环境
 
 $ conda env remove -n py3.7                                # 删除 py3.7 环境
 > Remove all packages in environment /root/anaconda3/envs/py3.7:
```

## 包管理

```bash
 $ conda list -n <name>               
 $ conda list -n py3.7                                      # 列出环境内所有包
 > # packages in environment at /root/anaconda3/envs/py39:
 > #
 > # Name  
 > ......

 $ conda install -n <name> <pkg1> <pkg2>                   # 指定环境安装包
 $ conda install -n  py39  toml  yaml                      # py39 环境安装 toml 和 yaml 包
 
 $ conda uninstall <pkg> -n <name>                         # 指定环境卸载包
 $ conda uninstall yaml -n py39

 $ conda update --all -n <name>                            # 指定环境更新所有包
```
