import re
s='     Python,武器库定制  \n'

print(re.findall('\s*(\w+)\s*',s))
#输出:['Python', '武器库定制']??这是为什么
