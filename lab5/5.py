import re
txt = "hello ab a123b xyz aXb aXY"
x = re.findall("a.*b", txt)
print(x)