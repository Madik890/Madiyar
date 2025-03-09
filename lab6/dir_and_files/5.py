import os
def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")
write_list_to_file("123.txt", ["Hello", "World"])           