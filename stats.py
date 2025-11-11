def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    characters = {}
    for i in text:
        i = i.lower()
        if i not in characters:
            characters[i] = 0
        characters[i] += 1
    return characters

# testing
# r = count_chars("assdkjfhisuabskdjnfiayuhrsfkkjnasmd")
# print(r)
