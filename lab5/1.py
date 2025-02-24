import re
txt = "ab acb a123b aXb aXY"
x = re.findall("a.*b", txt)
print(x) 
