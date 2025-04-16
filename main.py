def get_book_text(path_file: str) -> str:
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file = get_book_text("books/frankenstein.txt")
    print(file)

main()