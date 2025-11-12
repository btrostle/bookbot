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

def sort_on(list):
    return list['num']

def sort_chars(chars_dict):
    dicts = []
    for char in chars_dict:
        entry = {"char": char, "num": chars_dict[char]}
        dicts.append(entry)
    dicts.sort(reverse=True, key=sort_on)
    return dicts
# testing
# r = count_chars("assdkjfhisuabskdjnfiayuhrsfkkjnasmd")
# print(r)

#print(sort_chars(test_dict))
