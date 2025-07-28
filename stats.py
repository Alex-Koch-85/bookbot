import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    file_contents = get_book_text()
    word_list = file_contents.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")

def get_num_chars():
    chars_dict = {}
    file_contents = get_book_text()
    for char in file_contents:
        char = char.lower()
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def dict_list():
    chars_dict = get_num_chars()
    chars_dict_list = []
    for k, v in chars_dict.items():
        list_dict = {}
        list_dict["char"] = k
        list_dict["num"] = v
        chars_dict_list.append(list_dict)
    chars_dict_list.sort(reverse=True, key=sort_on)
    for dict in chars_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

def sort_on(items):
    return items["num"]

