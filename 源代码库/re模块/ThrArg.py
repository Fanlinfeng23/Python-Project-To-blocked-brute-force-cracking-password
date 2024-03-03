import re
s='Hello\n人生'
print(re.findall('Lo',s))
#输出[]


print(re.findall('Lo',s,re.I))
#输出['lo']



print(re.findall('Lo.',s,re.I))
#输出[]，因为'.'指的是匹配除换行符以外的


print(re.findall('Lo.',s,re.I|re.S))
#输出['lo\n'],用管道符|隔开
