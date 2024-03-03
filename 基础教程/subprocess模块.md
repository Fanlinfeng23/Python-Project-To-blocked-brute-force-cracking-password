# SUBPROCESS-LEARNING
[模块详情](https://docs.python.org/3/library/subprocess.html#module-subprocess)
> 项目需求：执行命令并将输出劫持，实现日志的监控

> 功能：用于启动新的进程模块，它可以用于执行外部命令，获取进程输出，向进程发送输入和等待进程结束

## 多进程协同，python里大概有三种方式：
1.os.system函数。缺点：阻塞式
2.multiprocessing 模块。使用场景：密集型计算场景
3.subprocess 模块。
## 主要函数
1.subprocess.run ：执行指定命令，等待命令执行后返回一个对象

> subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)

> args:要执行的命令，必须是字符串，字符串列表参数

> stdin，stdout，stderr ：子进程中的标准输入，输出，错误，最常用的值是：subprocess.PIPE

>timeout：设置命令超时 


2.subprocess.call：执行指定的命令，返回命令的执行状态

3.subprocess.check_call：（跟上面差不多）区别是会报错

4.subprocess.getoutput：执行命令返回结果 
