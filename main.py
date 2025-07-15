from stats import words_in_book


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_amount = words_in_book(book_text)
    print(book_text)
    print(f"{word_amount} words found in the document")

main()