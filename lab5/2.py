import re
txt = "abb abbb abbbb ab ab"
x = re.findall("ab{2,3}", txt)
print(x)