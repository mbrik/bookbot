def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def words_count(book_path):
    text = get_book_text(book_path)
    words = text.split()
    return len(words)


def chars_count(book_path):
    text = get_book_text(book_path)
    l_test = text.lower()
    cl_test = list(l_test)

    chars = {}
    for char in cl_test:
        if char in chars:
            chars[char] += 1
        else:
            chars.update({char : 1})

    return chars

def sort_on(items):
    return items["num"]

def char_stats(book_path):
    chat_dict = chars_count(book_path)
    char_dict_list = []
    
    for k, v in chat_dict.items():
        if k.isalpha():
            char_dict_list.append({"char": k, "num": v})
    
    char_dict_list.sort(key=sort_on, reverse=True)
    return char_dict_list

def print_char_stats(book_path):
    stats=char_stats(book_path)
    for i in range(len(char_stats(book_path))):
        print(f"{stats[i]["char"]}: {stats[i]["num"]}")

