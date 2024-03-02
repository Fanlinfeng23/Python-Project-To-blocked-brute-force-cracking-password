import re
s="hello 你好 520"
print(re.findall('hello',s))

#返回['hello']

print(re.findall('l',s))

#返回['l','l']
