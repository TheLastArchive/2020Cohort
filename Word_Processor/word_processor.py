import re

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """Takes a string of characters and puts them in a list split by the specified delimiters"""
    text = text.lower()
    out = []
    for i in re.split('[;,.?\s]\s*', text):
        if i != "": out.append(i)

    return out


def words_longer_than(length, text):
    """Takes a string of characters and returns a list of all words that are longer than the specified length"""

    text = convert_to_word_list(text)
    out = []
    for i in text:
        if len(i) > length: out.append(i)
    
    return out


def words_lengths_map(text):
    """Returns a dictionary of the amount of words there are of each length in a string"""

    text = convert_to_word_list(text)
    out = {}
    for i in text:
        if len(i) not in out: out[len(i)] = 1
        else: out[len(i)] += 1

    return out


def letters_count_map(text):
    
    text = "".join(convert_to_word_list(text))
    char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for i in text: char_count[i] += 1

    return char_count


def most_used_character(text):
    
    if text == "": return None

    text =  "".join(convert_to_word_list(text))
    if text.isalpha() == False: return None

    my_dict = letters_count_map(text)

    return max(my_dict, key = my_dict.get)

