def get_num_words(text: str) -> int:
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