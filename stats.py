def get_num_words(text):
    return len(text.split())

def get_num_chars_dict(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(dict):
    return dict["count"]

def get_sorted_chars(char_count):
    chars_list = [
        {
            "char": char,
            "count": count
        }
        for char, count in char_count.items()
    ]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list