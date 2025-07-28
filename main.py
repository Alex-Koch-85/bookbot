import sys
from stats import get_num_words, get_num_chars, dict_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("---------- Word Count ----------")    
        words = get_num_words()
        print("---------- Character Count ----------")
        chars = dict_list()

main()
