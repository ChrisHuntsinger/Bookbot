
#Returns the amount of words in a book
def words_in_book(book_words):
   return len(book_words.split())


#Calculates different characters in the book, and returns them.
#Uses a dictionary to do this in the way of ("char": amount_appears_in_book)
def chars_in_book(book_text):
    char_dict = {}

    for char in book_text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1

    return char_dict

def sort_on(item):
    return item["num"]

def sort_by_char_amount(char_dict):
    sortable_list = []

    for char, num in char_dict.items():
        sortable_list.append({"char": char, "num": num})

    sortable_list.sort(reverse = True, key = sort_on)

    return sortable_list

    