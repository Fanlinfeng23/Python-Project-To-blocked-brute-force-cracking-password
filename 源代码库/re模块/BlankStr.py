import re
s = '     \nPython武器库 \r'

print(re.findall('\s',s))
#由此可得出filter过滤的思路

print(re.findall('[^\s]',s))
#过滤掉无用字符，输出['P','y''t','h,'o','n','武','器','库']


#还有更简单的用法
print(re.findall('\S',s))
#根据上文大写输出内容往往是小写的补集可知，该次输出与前次输出相同


