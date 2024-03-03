import re
s = 'char_achar_b,char_cpythonchar_d 爱你##%'

print(re.findall('char_[ab]',s))
#输出['char_a','char_b']

print(re.findall('char_[^ab]',s))
#输出['char_c','char_d']

print(re.findall('char_[a-c]',s))
#输出a到c

print(re.findall('[^0-9a-zA-Z_]',s))
#匹配除数字、字母、下划线之外的所有元素

#强烈建议自己尝试一下
