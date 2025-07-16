def words_in_book(book_words):
   return len(book_words.split())

def chars_in_book(book_text):
    char_dict = {}
    for char in book_text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict


            