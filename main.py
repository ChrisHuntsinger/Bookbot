from stats import words_in_book
from stats import chars_in_book



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = words_in_book(book_text)
    amount_of_chars_in_book = chars_in_book(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"{word_amount} words found in the document")
    print("--------- Character Count -------")
    print(amount_of_chars_in_book)


main("books/frankenstein.txt")