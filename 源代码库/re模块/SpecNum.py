import re

s = 'hell#hello$helloo@'

print(re.findall('hello*',s))
#按上面说的匹配‘*’前一个字符‘o'的0-无限次
#输出:['hell', 'hello', 'helloo']

 print(re.findall('hello+',s))
 #按上面说的匹配‘*’前一个字符‘o'的1-无限次
 #输出:['hello', 'helloo']


