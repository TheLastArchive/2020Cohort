
def find_min(element):
    """TODO: complete for Step 1"""
    
    if len(element) == 0: return -1
    for x in element:
        if isinstance(x, int) == False: return -1

    if len(element) == 1: return

    elif element[0] < element[1]: 
        element.pop(1)
        find_min(element)
    else: 
        element.pop(0)
        find_min(element)

    return element[0]


def sum_all(element):
    """TODO: complete for Step 2"""
    
    if len(element) == 0: return -1
    for x in element:
        if isinstance(x, int) == False: return -1

    if len(element) == 1: return

    else:
        element[0] = element[0] + element[1]
        element.pop(1)
        sum_all(element)

    return element[0]


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    pass

