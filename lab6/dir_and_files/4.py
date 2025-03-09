def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"Line count: {sum(1 for _ in f)}")
    except FileNotFoundError:
        print("File not found.")
count_lines_in_file("123.txt")        