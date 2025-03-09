import shutil
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print("File not found.")
copy_file("A.txt", "B.txt")        