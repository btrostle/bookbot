import sys
from stats import * 

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f'============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------')
    contents = get_book_text(filepath)
    print(f'Found {count_words(contents)} total words')
    chars_dict = count_chars(contents)
    sorted_dict = sort_chars(chars_dict)
    print(f'--------- Character Count -------')
    for char in sorted_dict:
        if char['char'].isalpha():
            print(f'{char['char']}: {char['num']}')


main()
