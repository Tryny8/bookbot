def get_book_text(path_file: str) -> str:
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents

def count_word(text: str) -> int:
    list_word = []
    list_word_raw = text.split(" ")
    for word in list_word_raw:
        if word != '':
            if '\n' in word:
                temp = word.split("\n")
                for element in temp:
                    if element != '':
                        list_word.append(element)
            else:
                list_word.append(word)
    count = len(list_word)
    return count

def main():
    file = get_book_text("books/frankenstein.txt")
    num_words = count_word(file)
    print(f"{num_words} words found in the document")

main()