import sys
from stats import get_num_words, get_num_caract, sort_dict


def get_book_text(path_file: str) -> str:
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(file, count_word, list_caract):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_word} total words")
    print("--------- Character Count -------")
    for dico in list_caract:
        if dico["caract"].isalpha():
            print(f"{dico["caract"]}: {dico["num"]}")
    print("============= END ===============")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_file = sys.argv[1]
    str_file = get_book_text(path_file)
    num_words = get_num_words(str_file)
    num_caract = get_num_caract(str_file)
    sorted_caract = sort_dict(num_caract)
    print_report(path_file, num_words, sorted_caract)

main()