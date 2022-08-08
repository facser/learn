<!--
 * @FilePath: \文档\Learning\Linux\Linux-4-system.md
 * @Author: facser
 * @Date: 2022-07-18 15:02:16
 * @LastEditTime: 2022-08-08 22:14:46
 * @LastEditors: facser
 * @Description: 
-->

# Linux system

### 系统

#### [uname](https://linux.alianga.com/c/uname.html) : Unix name

```bash
 $ uname -a                                      # 打印操作系统的所有信息
```

#### [date](https://linux.alianga.com/c/date.html) 

```bash
 $ date                                          # 现实系统时间
 $ date +"%Y-%m-%d %H:%M:%S"                     # 格式化输出时间
 $ date -s "01:01:01 2022-08-09"                 # 设置时间
```

#### [df](hthttps://linux.alianga.com/c/df.html) : disk free

```bash
 $ df                                            # 显示系统磁盘占用信息
 $ df -h                                         # 容量信息添加单位
```

#### [du](https://linux.alianga.com/c/du.html) : disk usage

```bash
 $ du <arg> <file>                               # 显示目录占用空间大小
 $ du -s <file>                                  # --summarize 只显示总计占用
 $ du -h <file>                                  # --human-readable 添加单位
```

#### [free](https://linux.alianga.com/c/free.html) : Unix name

```bash
 $ free                                          # 显示系统内存占用(KB)
 $ free -m                                       # 以 MB 为单位显示
 $ free -g                                       # 以 GB 为单位显示
```

#### [ps](https://linux.alianga.com/c/ps.html) : process status

```bash
 $ ps <opt>                                      # 显示系统进程状态
 $ ps aux                                        # 显示系统所有进程的详细信息
```

#### [systemctl](https://linux.alianga.com/c/systemctl.html) : systemctl control

```bash
 $ systemctl <opt> <service>                     # 设置某项服务
 $ systemctl start <service>                     # 启动nfs服务
 $ systemctl enable <service>                    # 设置开机自启动
 $ systemctl disable <service>                   # 停止开机自启动
 $ systemctl status <service>                    # 查看服务当前状态
 $ systemctl restart n<service>                  # 重新启动某服务
 $ systemctl list-units --type=service           # 查看所有已启动的服务
```

#### [netstat]() : network statistics

```bash
 $ netstat <opt>                                 # 显示网络端口信息
 $ netstat -a                                    # 显示所有网络端口信息
 $ netstat -t                                    # 显示 TCP 网络端口信息
 $ netstat -u                                    # 显示 UDP 网络端口信息
 $ netstat -l                                    # --listening 显示处于监听状态的端口
```
