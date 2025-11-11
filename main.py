from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    contents = get_book_text('books/frankenstein.txt')
    print(f'Found {count_words(contents)} total words')
    print(count_chars(contents))

main()
