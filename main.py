from stats import words_in_book
from stats import chars_in_book
from stats import sort_by_char_amount
import sys


if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):    
    book_text = get_book_text(path_to_file)
    word_amount = words_in_book(book_text)
    amount_of_chars_in_book = chars_in_book(book_text)
    sorted_chars = sort_by_char_amount(amount_of_chars_in_book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_amount} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ==============")

main(sys.argv[1])