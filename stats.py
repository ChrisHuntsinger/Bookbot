def words_in_book(book_words):
   return len(book_words.split())

def chars_in_book():
    char_dict = {}
    for char in book_text:
        if char not in char_dict:
            char_dict[char] = 1
        
            