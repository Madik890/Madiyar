import re
txt = "hello_world test_case Hello_World snake_case"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)  
