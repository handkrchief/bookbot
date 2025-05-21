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

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    
    new_list = []

    for key in dict:
        new_dict = {"char": key, "num": dict[key]}
        new_list.append(new_dict)

    new_list.sort(reverse=True, key=sort_on)
    return new_list
    