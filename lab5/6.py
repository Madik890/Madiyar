import re
txt = "Hello, world. This is a test string."
x = re.sub("[ ,.]", ":", txt)
print(x)