import re

s='hello 你好 520'

m = re.search('hello',s)

print(m.group())
#输出 hello

print(m.span())
#输出字符串长度和位置(0,5)

n=re.search('l',s)

print(n.group())
#只输出一个l（对比findall输出两个l）

print(n.span())
#输出（2，3）

