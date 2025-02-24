import re
txt = "SplitAtUppercaseLetters"
x = re.split("(?=[A-Z])", txt)
print(x)