# Given a string, splits the text and counts the number of entries in the list (word count)
def count_words(text):
    split_text = text.split()
    return len(split_text)


def count_characters(text):
    lower_string = text.lower()
    char_dict = {}
    for char in lower_string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict
