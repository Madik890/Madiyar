import re
txt = "Hello Python java Test123 aB"
x = re.findall("[A-Z][a-z]+", txt)
print(x)