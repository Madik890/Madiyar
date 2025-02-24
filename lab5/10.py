import re
camel_case = "helloWorldExample"
snake_case = re.sub("(?<!^)(?=[A-Z])", "_", camel_case).lower()
print(snake_case)  
