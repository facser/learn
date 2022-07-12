<!--
 * @FilePath: \learn\git.md
 * @Author: facser
 * @Date: 2022-07-08 10:17:53
 * @LastEditTime: 2022-07-12 12:16:42
 * @LastEditors: facser
 * @Description: 
-->
# git

详细的命令解释查询
[linux 命令大全](https://www.linuxcool.com/)
[linux 搜索引擎](https://linux.utils.fun/)

## git 安装

### 检查 git 是否安装

```bash
 $ git --version 
 > git version 1.8.3.1
```

### 安装

- Centos Redhat 系统使用 yum 安装 git

```bash
 $ yum install git
```

- Ubuntu Debian 系统使用 apt

```bash
 $ apt-get install git
```

## git 配置

### 检查 system global local 配置

查看所有配置及其所在的文件, 早期版本不支持此命令

```bash
 $ git config --list --show-origin
```

查看各级别 git 配置信息

```bash
 $ git config --system --list      # 查看系统的 git 配置
 $ git config --global --list      # 查看系统用户的 git 配置
 $ git config --local --list       # 查看当前库 的 git 配置
 $ git config --list               # 列出上述所有配置, 可能出现重复项
```

- system: /etc/gitconfig 文件, 包含系统上每一个用户及他们仓库的通用配置, 如果在执行 git config 时带上 --system 选项，那么它就会读写该文件中的配置变量.
- global: ~/.gitconfig 或 ~/.config/git/config 文件, 只针对当前用户, 你可以传递 --global 选项让 Git 读写此文件，这会对你系统上 所有 的仓库生效.
- local: 当前使用仓库的 Git 目录中的 config 文件（即 .git/config）, 针对该仓库, 你可以传递 --local 选项让 Git 强制读写此文件, 虽然默认情况下用的就是它

相同的配置, 优先使用范围小的配置 local > global > system

### 选择查看配置

```bash
 $ git condig <key>      

 $ git config user.name
 > facser
```

### 添加用户信息

为当前系统用户添加用户信息

```bash
 $ git config --global user.name "<user.name>"    
 $ git config --global user.email "<mail>"
```

为当前库添加用户信息, 库的配置会覆盖系统配置中相同的部分

```bash
 $ git config --local user.name "<user.name>"
 $ git config --local user.email "<mail>"
```

### 修改 git 常用配置

- 编辑器

```bash
 $ git config --global core.editor vim 
```

- commit 模板

```bash
 $ git config --global commit.template  <file>
```

## git 仓库

### 本地创建仓库

```bash
 $ git init
```

该命令将在当前目录创建一个名为 .git 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件。 该命令是一个初始化的操作，还未对文件追踪。

### github 创建仓库克

在 github 创建仓库后，将仓库克隆到本地

```bash
 $ git clone <Repository url>
```

### 本地仓库关联 github 仓库

github 上必须先创建一个仓库, 才可以将本地代码上传到 github

```bash
 $ git init                                    # 初始化本地仓库
 $ git add --all                               # 追踪目录下所有文件修改
 $ git commit -m "<commit message>"            # 记录修改生成一个版本到本地仓库
 $ git remote origin add <Repository url>      # 将远程仓库命名 origin 并关联本地仓库
 $ git push -u origin master                   # 提交代码到 origin 仓库 master 分支
```

- 本地仓库可以关联多个远程仓库
- 本地仓库可以指定提交到某个远程仓库
- 第一远程仓库默认命名为 origin

## 本地仓库操作

工作区 -- git add --> 暂存区 -- git commit --> 本地仓库

### git add

将工作区的修改保存至暂存区, 追踪修改内容

```bash
 $ git add <file>     # 记录指定文件修改
 $ git add .          # 记录当前目录下所有文件修改(上层文件未记录)
 $ git add --all      # 记录当前项目所有文件修改(推荐)
```

### git diff


### git status

查看当前状态

```bash
 $ git status -s           # -s --short 显示简略信息
 > M  README               # 表示该文件已 add 和 commit
 > MM Rakefile             # 已 commit 的文件 最新的修改未 add
 > A  lib/git.rb           # 从未 commit 但已 add 
 > AM lib/git.md           # 从未 commit 但 add 过, 最新修改未 add 
 > ?? LICENSE.txt          # 未 add 未追踪的文件
```

左边有字母表示已 add, 进入暂存区, M 表示 commit 过, A 表示未 commit 过
右边有字母表示最新的修改未 add 进入暂存区

### .gitignore

忽略指定文件, 不对其追踪和提交, 文件名固定为 .gitignore, 同项目可创建多个

```bash
 $ cat .gitignore
 > *.pyc              # 忽略当前项目内所有 .pyc 结尾的文件
 > !main.pyc          # 强制跟踪所有 main.pyc
 > /*.log             # 忽略当前目录下 .log 结尾文件, 不影响上层的文件
 > temp/              # 忽略整个项目内所有 temp 文件夹
 > /lib/*.pyc         # 忽略当前 lib 目录 下一级的 pyc 文件, lib 下多层目录不受影响  
 > lib/**/.pyc        # 忽略项目内所有 lib 文件夹内的 pyc 文件
```

## SSH key 密钥

本地系统创建公钥和私钥, 将公钥内容复制到 github 账户 SSH key 设置, 将系统与 github 账户绑定
绑定后系统可以通过 ssh 方式下载账户下的代码且 push 代码时无需输入密码

### 生成密钥

- id_rsa (私钥)
- id_rsa.pub (公钥)

使用以下命令生成密钥, 生成时会显示存放为
一般为 /root/.ssh/id_rsa  /root/.ssh/id_rsa.pub

```bash
 $ ssh-keygen                             # 自动生成密钥
 $ ssh-keygen -t rsa -C "<user.mail>"     # 生成 rsa 类型带邮箱注释信息的密钥
```
