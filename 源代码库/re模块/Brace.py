import re

s = 'hvv windows git python java'

print(re.findall('[a-z]{3}',s))
#输出：['hvv', 'win', 'dow', 'git', 'pyt', 'hon', 'jav']

print(re.findall('[a-z]{3,6}',s))
#将字符串长度为三到六位的输出出来：['hvv', 'window', 'git', 'python', 'java']
