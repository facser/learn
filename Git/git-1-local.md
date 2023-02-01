# Git Local repository

## 介绍

本地仓库是

## 创建

使用 `git init` 创建本地仓库, 在创建位置会创建 .git 隐藏文件夹
仓库所有配置及版本文件均保存在 .git 文件夹中

```bash
 $ mkdir -p ~/Desktop/repository                 # 在左面创建 repository 文件夹 
 $ cd ~/Desktop/repository                       # 进入 repository 文件夹

 $ git init                                      # 在 repository 目录下创建本地仓库
 > Initialized empty Git repository in /root/Desktop/repository/.git/

 $ ls -a                                         # 查看创建的隐藏文件夹
 > .  ..  .git
```

## 状态

> git-status - Show the working tree status

git 用一下3种描述表示**文件状态**, 进一步可划分为**未追踪**和**已追踪**
工作区 -- `git add` --> 暂存区 -- `git commit` --> 本地仓库

|区域|描述|状态|
|:--:|:--:|:--:|
|`Untracked files`|新增文件|文件处于工作区, 未被追踪|
|`Changes not staged for commit`|有新修改的文件|文件处于工作区, 新修改未被追踪|
|`Changes to be committed`|无修改的文件|文件处于暂存区, 修改已追踪|

1. 新增文件

```bash
 $ touch first_file.txt                          # 在 repository 创建新文件 first_file.txt  
 
 $ git status                                    # 查看状态, 有新增文件未被记录
 > Untracked files:
        first_file.txt
```

2. 新增修改

> git-add - Add file contents to the index

```bash
 $ git add <file>                                # 记录指定文件修改
 $ git add .                                     # 记录当前目录下所有文件修改(上层文件未记录)
 $ git add --all                                 # 记录仓库目录下所有文件修改(推荐)
```

```bash
 $ git add --all                                 # 记录 repository 目录下所有修改

 $ git status                                    # 新增文件已被记录
 > Changes to be committed:
        new file:   first_file.txt
```

```bash
 $ echo "first change" >> first_file.txt         # 修改文件内容

 $ git status                                    # 查看状态
 > Changes to be committed:
        new file:   first_file.txt

  Changes not staged for commit:
        modified:   first_file.txt

 $ git add --all                                 # 记录所有修改
 $ git status                                    # 查看状态, 新修改已被记录
 > Changes to be committed:
        new file:   first_file.txt
```

> git-commit - Record changes to the repository



当一个文件通过 `git add` 追踪后, 又修改了, 此时查看 `git status` 会如何显示？

```bash
 $ git status
 >Your branch is up to date with 'origin/main'.
 >
 >Changes to be committed:                
 >        modified:   README.md           
 >        modified:   git.md                     # git.md 已被追踪, 保存的是已追踪时内容
 >
 >Changes not staged for commit:          
 >        modified:   git.md                     # 新修改未被追踪
```

通过过上面结果可知, 只要文件存在未被追踪的内容就会归入到工作区

```bash
 $ git status -s                                 # -s --short 显示简略信息
 > M  README                                     # 表示该文件已 add 和 commit, 未再修改
 > A  lib/git.rb                                 # 从未 commit 但已 add, 未再修改
 > MM Rakefile                                   # 已 commit 的文件, 最新的修改未 add
 > MD temp.txt                                   # commit 过, 当前已删除, 未 add 记录删除 
 > AM lib/git.md                                 # 从未 commit 但 add 过, 最新修改未 add
 > ?? LICENSE.txt                                # 未 add 未追踪的文件
```

|缩写|位置        |详细               |
|:-- |:--        |        :--:       |
|??  |工作区      |新增文件, 从未被追踪|
|AM  |工作区 暂存区| 未进入过本地仓库   |
|MM  |工作区 暂存区| 进入过仓库        |
|MD  |暂存区      | 进入过仓库         |
|A   |暂存区      | 未进入本地仓库     |
|M   |暂存区      | 进入过本地仓库     |

右边有字母表示有修改未追踪, 在工作区显示(删除文件不显示)
左边有字母表示已追踪, 无修改, M 表示 commit 过, A 表示未 commit 过

### [git add](https://git-scm.com/docs/git-add)