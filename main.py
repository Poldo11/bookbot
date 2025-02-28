import sys
from stats import get_num_words, get_num_chars_dict, get_sorted_chars




book_name = sys.argv[1]
def get_book_text(book_name):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(f"{book_name}") as f:
        return f.read()

def main(book_name):
    text = get_book_text(book_name)
    char_count = get_num_chars_dict(text)
    sorted_chars = get_sorted_chars(char_count)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_name}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print(f"--------- Character Count -------")
    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['count']}")
    print(f"============= END ===============")

main(book_name)