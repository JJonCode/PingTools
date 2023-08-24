# 一个用于地址连通率测试、丢包数据解析的Ping工具。

## 依赖
该项目使用poetry作为软件包依赖管理工具，python版本需大于3.10

## 使用方法：
### 获取帮助
    python ping_tools.py -h
可在任意二级指令下附带"-h"获取该指令帮助。
### Ping
    python ping_tools.py ping $host $wait
host: 指定ping地址，默认为127.0.0.1

wait: 指定每次执行ping后的等待时长，默认为1秒

### 日志解析
    python ping_tools.py loss --filename [FILENAME]  --type [TYPE]
FILENAME: 指定解析日志文件名，默认为最后一次使用ping工具获取到的日志文件，指定日志文件仅需输入logs文件夹下的日志文件名即可

TYPE：指定解析功能，默认为print，可选参数：
 - print：显示当前日志中各小时的丢包数
 - top3：获取日志中每日最多丢包数前三的小时及丢包数量
 - min3：获取日志中每日最少丢包数前三的小时及丢包数量
