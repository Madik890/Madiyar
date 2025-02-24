import re
txt = "InsertSpacesBetweenWords"
x = re.sub("(?=[A-Z])", " ", txt)
print(x)