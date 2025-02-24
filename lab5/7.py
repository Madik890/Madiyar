import re
snake_case = "hello_world_example"
camel_case = re.sub('_([a-z])', lambda m: m.group(1).upper(), snake_case)
print(camel_case)  
