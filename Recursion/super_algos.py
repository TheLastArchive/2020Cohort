
def find_min(element):
    """Goes through a list of integers recursively and returns
    the smallest value """
    
    if len(element) == 0: return -1
    for x in element:
        if isinstance(x, int) == False: return -1

    if len(element) == 1: return element[0]

    elif element[0] < element[1]: 
        element.pop(1)
        find_min(element)
    else: 
        element.pop(0)
        find_min(element)

    return element[0]


def sum_all(element):
    """Goes through a list of integers recursively and returns the some of
    all elements"""
    
    if len(element) == 0: return -1

    for x in element:
        if isinstance(x, int) == False: return -1

    if len(element) == 1: return element[0]

    else:
        element[0] = element[0] + element[1]
        element.pop(1)
        sum_all(element)

    return element[0]


def find_possible_strings(character_set, n):
    """Pain. This function causes pain."""

    character_set = list(character_set)
    
    for x in character_set:
        if len(character_set) == 0 or isinstance(x, str) == False: return []
    
    if len(character_set) == 1: return character_set[0] * n

    else:
        result = find_perms(character_set, n, "",[])

    return result


def find_perms(character_set, n, char, result):
    """This function helps ease the pain by finding all permutations"""

    new = ""
    count = 0

    if n == 0:
        result.append(char)
        return

    while count < len(character_set):
        new = char + character_set[count]
        find_perms(character_set, n-1, new, result)
        count += 1

    return result
