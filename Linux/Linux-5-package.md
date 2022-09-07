
# Linux package

## 包管理工具

### Centos Redhat

#### [yum](https://linux.alianga.com/c/yum.html) : YellowdogUpdater,Modified

```bash
 $ yum <opt> <pack>                              # RedHat Centos 包管理工具

 $ yum install <pack>                            # 下载安装包
 $ yum update <pack>                             # 更新已安装的包    
 $ yum remove <pack>                             # 卸载已安装的包
 $ yum search <pack>                             # 检查软件包的信息

 $ yum list                                      # 列出所有已安装的包
 $ yum list installed <pack>                     # 检查包是否安装
 
```

注: yum 配置文件 `/etc/yum.repos.d/`

#### [rpm](https://linux.alianga.com/c/rpm.html) : RedHat Package Manager

```bash
 $ rpm <opt> <pack>

 $ rpm -i <pack>                                 # 安装 rpm 包
       -v                                        # 显示安装信息
       -h                                        # 安装包时列出标记
       -e                                        # 卸载 rpm 包

$ rpm -ivh <pack>                                # 安装 rpm 包, 显示安装过程
```

### Ubuntu

#### [apt-get](https://linux.alianga.com/c/apt-get.html) : Advanced Package Tool get

```bash
 $ apt <opt> <pack>

 $ apt-get install <pack>                        # 下载并安装软件包
 $ apt-get remove <pack>                         # 卸载已安装的软件包
 
 $ apt-get upgrade                               # 更新所有已安装的软件包
 $ apt-get update                                # 更新软件包列表

 $ apt install <pack>                            # apt 集成 apt-get 功能
 $ apt download <pack>                           # 仅下载包, 不安装   
 $ apt search <pack>                             # 查找 包
 $ apt remove <pack>                             # 卸载已安装的包  

 $ apt list install                              # 列出已安装的包
```

注: OS 默认下载源文件 `/etc/apt/source.list`

#### [dpkg](https://linux.alianga.com/c/dpkg.html) : Debian package

```bash
 $ dpkg <opt> <pack>

 $ dpkg -i <pack>                                # 安装 deb 安装包
 $ dpkg -r <pack>                                # 卸载 deb 包

 $ dpkg -l                                       # 列出所有安装的包
```

## 压缩 解压

#### [tar](https://linux.alianga.com/c/tar.html)

```bash
 $ tar <opt> <pack>                         

 $ tar -zxvf <tar.gz> -C <dir>                   # 解压 tar.gz 包到 <dir> 路径
 $ tar -zcvf <tar.gz> <file|dir>                 # 将文件或目录压缩

 $ tar -ztvf <tar.gz>                            # 列出压缩包的文件
```

#### [zip](https://linux.alianga.com/c/zip.html)

```bash
 $ zip <opt> <pack>


 $ zip <zip> <file>                              # 压缩文件成 zip 包
 $ zip -r <zip> <dir>                            # 压缩目录成 zip 包

 $ unzip <zip>                                   # 解压文件
 $ unzip -v <zip>                                # 查看压缩文件内容
```
