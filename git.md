<!--
 * @FilePath: \文档\Learning\git.md
 * @Author: facser
 * @Date: 2022-07-08 10:17:53
 * @LastEditTime: 2022-07-13 23:01:13
 * @LastEditors: facser
 * @Description: 
-->
# Git

结合以下网站阅读分析, 体验更佳
[Git 官方文档](https://git-scm.com/book/zh/v2)
[linux 命令大全](https://www.linuxcool.com/)
[linux 搜索引擎](https://linux.utils.fun/)

## Git 介绍

> Git is a free and open source distributed version control system designed to
> handle everything from small to very large projects with speed and efficiency

Git 是一个开源的版本控制器, 常被用来作为代码的搬运工, 记录员, 时光机.

- 搬运工: 可以把代码运输到指定位置保存
- 记录员: 记录代码和文件的改动
- 时光机: 回退代码到某一个记录过的状态

## Git 安装

### 检查 git 是否安装

```bash
 $ git --version 
 > git version 1.8.3.1
```

### [Git 官网](https://git-scm.com/)

```bash
 $ yum install git           # Centos Redhat 系统使用 yum 安装
 $ sudo apt-get install git  # Ubuntu Debian 系统使用 apt
```

## Git 配置

### Git 配置分类

一个系统可以有多个用户, 每个用户可以创建多个代码仓库
由此 git 配置根据范围可以分为 `system`, `global`, `local` 3种
相同的设置项, 优先使用范围小的配置 `local` > `global` > `system`

|leve|file|introduce|
|:--:|:--:|:--|
|system|`/etc/gitconfig`|系统上每一个用户及他们仓库的通用配置(不常用)|
|global|`~/.gitconfig`|当前系统用户, 这会对你系统上所有的仓库生效|
|local|`.git/config`|针对仓库, 在仓库内默认使用 local 配置|

### [git config](https://git-scm.com/docs/git-config)

> git-config - Get and set repository or global options

```bash
 $ git config --list --show-origin  # 查看所有配置及所在的文件, 早期版本不支持
```

```bash
 $ git config --system --list      # 查看系统的 git 配置
 $ git config --global --list      # 查看系统用户的 git 配置
 $ git config --local --list       # 查看当前库的 git 配置
 $ git config --list               # 列出上述所有配置, 可能出现重复项
```

```bash
 $ git config <key>                # 查看某项配置的值 

 $ git config user.name            # 查看当前用户名
 > facser
```

```bash
 $ git config --global user.name "<user.name>"   # 设置系统用户的用户名
 $ git config --global user.email "<mail>"       # 设置系统用户邮箱
```

```bash
 $ git config --local user.name "<user.name>"    # 设置仓库用户名
 $ git config --local user.email "<mail>"        # 设置仓库用户邮箱
```

```bash
 $ git config -e                                 # 编辑配置文件
 $ git config --global core.editor vim           # 设施编辑器
 $ git config --global commit.template <file>    # 设置 commit 模板
```

## Git 仓库

### 介绍

|区域|位置|介绍|
|:--:|:--:|:--:|
|本地仓库|本地| 记录文件当前状态生成一个版本并保存至本地仓库|
|远程仓库|代码托管网站| 将当前记录的版本上传到远程仓库|

### 本地仓库

创建本地仓库

```bash
 $ git init   # 在当前目录创建.git 子目录(包含仓库所有 git 文件与版本数据)
```

### [git status](https://git-scm.com/docs/git-status)

> git-status - Show the working tree status

工作区 -- `git add` --> 暂存区 -- `git commit` --> 本地仓库

|区域|命令|介绍|
|:--:|:--:|:--:|
|工作区|add 前|未追踪的文件, 未追踪的修改都处于工作区|
|暂存区|add 后 commit 前|当前所有状态已保存, 可以准备生成新版本|
|本地仓库|commit 后|已生成一个版本保存到本地仓库|

注: 工作区和暂存区表示的是文件的状态, 当一个文件当前状态没有被记录或者与之前状态不同, 那么它就在
工作区, 使用 `git add` 记录一下之后, 它就移动到暂存区, 此时修改它, 它又会回到工作区.

```bash
 $ git status
 >Your branch is up to date with 'origin/main'.
 >
 >Changes to be committed:                # 表示暂存区, 已经记录两个文件
 >        modified:   README.md           
 >        modified:   git.md
 >
 >Changes not staged for commit:          # 表示工作区, 存在未被记录的修改
 >        modified:   git.md
```

暂存区有 `README.md`, 工作区没有, 表示该文件已被记录且之后未修改
暂存区、工作区都有 `git.md` 表示该文件被记录过, 但最新的修改没有被记录

```bash
 $ git status -s           # -s --short 显示简略信息
 > M  README               # 表示该文件已 add 和 commit, 未再修改
 > A  lib/git.rb           # 从未 commit 但已 add, 未再修改
 > MM Rakefile             # 已 commit 的文件, 最新的修改未 add
 > MD temp.txt             # commit 过, 当前已删除, 未 add 记录删除 
 > AM lib/git.md           # 从未 commit 但 add 过, 最新修改未 add
 > ?? LICENSE.txt          # 未 add 未追踪的文件
```

|缩写|位置|详细|
|:--|:--|:--:|
|??|工作区|新增文件, 从未被追踪|
|AM|工作区、暂存区| 未进入过本地仓库|
|MM|工作区、暂存区| 进入过仓库|
|MD|暂存区| 进入过仓库|
|A |暂存区| 未进入本地仓库|
|M |暂存区| 进入过本地仓库|

右边有字母表示最新修改未 add 进行记录, 在工作区显示(删除文件不显示)
左边有字母表示已 add 过修改, 在缓存区显示
左M 表示 commit 过
左A 表示未 commit 过

### [git add](https://git-scm.com/docs/git-add)

> git-add - Add file contents to the index

追踪文件或修改, add 之后文件会进入暂存区

```bash
 $ git add <file>          # 记录指定文件修改
 $ git add .               # 记录当前目录下所有文件修改(上层文件未记录)
 $ git add --all           # 记录当前项目所有文件修改(推荐)
```

### [git diff](https://git-scm.com/docs/git-diff)

> git-diff - Show changes between commits, commit and working tree, etc

比对工作区文件和暂存区文件, 即未被记录的内容和被记录的内容比对, 即状态为
`AM` `MM` 状态的文件才会比对, 未被记录过或无修改的文件不显示

```bash
 $ git diff
 > diff --git a/test.log b/test.log             # 比对 test.log 文件两个状态
 > index 61e2b58..9b6b46c 100644
 > --- a/test.log                               # - 开头是修改前内容
 > +++ b/test.log                               # + 开头是修改后内容
 > @@ -1 +1,1 @@
 > -git add once                                # 修改前是 git add once
 > \ No newline at end of file
 > +before second add run git diff              # 修改后变成 before second add run git diff
 > \ No newline at end of file
```

### [git commit](https://git-scm.com/docs/git-commit)

> git-commit - Record changes to the repository

根据暂存区所有记录的文件生成一个版本并放入本地仓库
每 commit 一次便生成了一个可以回溯的点, 以便于版本回退

```bash
 $ git commit -m "<commit message>"    # message 较短可直接填写
 $ git commit -s                       # message 较长, 使用默认编辑器编辑 commit
 $ git commit --amend                  # 在上次 commit 基础上修改, 并替换原来的 commit
 $ git commit --amend --no-edit        # 使用上次 commit 且不修改, 即本次 commit 和上次合并

 $ git checkout -- <file>              # 撤销工作区的修改, 回到上次 commit 状态
```

注: 可通过 `git config --global core.editor vim` 修改编辑器为 `vim`

### [git log](https://git-scm.com/docs/git-log)

> git-log - Show commit logs

查看各 commit 版本信息, 即所有可以回溯的点

```bash
 $ git log                     # 显示所有 commit 的版本的详细信息
 $ git log --pretty=oneline    # 显示 commit 版本的简略信息
```

### [git reset](https://git-scm.com/docs/git-reset)

> git-reset - Reset current HEAD to the specified state

通过 `git log` 定位回退的版本, 使用 `git reset` 执行回退

```bash
 $ git reset --hard HEAD^                 # 回退到上个版本
 $ git reset --hard HEAD <commit number>  # 回到指定 commit 版本
```

### 远程仓库

创建远程仓库需要登录代码托管平台创建仓库, 然后将仓库克隆到本地, 或者将本地仓库
与远端仓库关联

- 本地仓库可以关联多个远程仓库
- 本地仓库可以提交代码到任意一个已关联的远程仓库
- 使用克隆后, 改远程仓库默认被命名为 origin

```bash
 $ git clone <Repository url>    # 克隆远端仓库到本地

 $ git remote -v                 # 查看本地仓库关联的所有远端仓库
```

```bash
 $ git init                                  # 初始化本地仓库
 $ git add --all                             # 追踪目录下所有文件修改
 $ git commit -m "<commit message>"          # 记录修改生成一个版本到本地仓库
 $ git remote origin add <Repository url>    # 将远程仓库命名为 origin 并关联本地仓库
```

### [git push](https://git-scm.com/docs/git-push)

> git-push - Update remote refs along with associated objects

将本地所有新增的 commit 推送到远端仓库

```bash
 $ git push origin master     # 提交所有 commit 到 origin 仓库的 master 分支
 $ git push -u origin master  # 将 origin 仓库 master 分支作为拉取和推送的默认值

 $ git push <repo> <branch>   # 使用过 -u 后可以省略仓库和分支
```

## 常规流程

```bash
 $ git clone <repo url>                # 克隆远端仓库到本地
 $ git add --all                       # 修改完后, 记录所有修改
 $ git commit -m "<commit message>"    # 推送到本地仓库
 $ git push -u origin master           # 将本地版本提交到远端仓库

 $ git commit -a -m "<commit message>" # 同时记录修改并推送到本地仓库
```

## 分支

开发新需求时候为了不影响原有代码, 一般会先做备份, 在备份上开发验证
即使失败也可重新备份源代码, 也不影响原有代码

git 中通过分支来完成上述操作

```bash
 $ git branch                     # 查看所有分支及当前分支所处
 > * master
 >   fluid

 $ git branch <branch name>       # 创建一个分支
 
 $ git checkout <branch name>     # 跳转到<branch name>分支
 $ git checkout -b <branch name>  # 创建分支并跳转到该分支 
```

当分支代码验证后, 便可以将分支的代码合并到主分支
到主分支使用 `git merge <branch name>` 便可以将指定分支合并到主分支 

```bash
 $ git merge <branch name>     # 将 <branch name> 分支合并到当前所处分支
```

## .gitignore

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

本地仓库推送代码到远端时, git 会要求用户输入用户名和密码, 使用 ssh key 即可免密码推送

本地系统创建公钥和私钥, 将公钥内容复制到托管网站账户的 SSH key 设置, 将本地系统与网站账
户绑定, 绑定后系统可以通过 ssh 方式克隆账户下的代码且 push 代码时无需输入密码

### 生成密钥

|密钥|位置|
|:--:|:--:|
|id_rsa (私钥)|`/root/.ssh/id_rsa`|
|id_rsa.pub (公钥)|`/root/.ssh/id_rsa.pub`|

```bash
 $ ssh-keygen                             # 自动生成密钥
 $ ssh-keygen -t rsa -C "<user.mail>"     # 生成 rsa 类型带邮箱注释信息的密钥
```
