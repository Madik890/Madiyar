import string
def create_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w', encoding='utf-8') as f:
            f.write(f"This is {letter}.txt")
create_alphabet_files()            