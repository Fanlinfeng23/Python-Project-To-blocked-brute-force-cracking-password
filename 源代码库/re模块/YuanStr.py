import re

s='abcdefg_123456\nGPT%# 爱你'

print(re.findall('\d',s))
#输出['1','2','3','4','5','6']

print(re.findall('\D',s))
#输出除上一次输出的其他所有字符

print(re.findall('\W',s))
#输出特殊字符['\n','%','#',' ']
#若小写w则除W输出外其他元素，此处例略可以自行尝试。注意：小写同时输出下划线

