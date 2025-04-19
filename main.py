from stats import get_num_words, get_num_caract


def get_book_text(path_file: str) -> str:
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(file)
    print(f"{num_words} words found in the document")
    num_caract = get_num_caract(file)
    print(num_caract)

main()