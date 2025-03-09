import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} deleted.")
    else:
        print("File cannot be deleted.")
delete_file("C.txt")        