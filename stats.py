from operator import itemgetter

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

def get_num_caract(text_raw: str) -> dict:
    caract_dict = {}
    text: str = text_raw.lower()
    for caract in text:
        if caract in caract_dict:
            caract_dict[caract] = caract_dict[caract] + 1
        else:
            caract_dict[caract] = 1
    return caract_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(caract_raw_dict: dict) -> list[dict]:
    tmp_caract_list: list[dict] = []
    sorted_caract_list: list[dict] = []
    for key, value in caract_raw_dict.items():
        tmp_caract_list.append({"caract": key, "num": value})
    sorted_caract_list = sorted(tmp_caract_list, key=itemgetter('num'), reverse=True)
    return sorted_caract_list