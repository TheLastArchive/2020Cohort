import os

DEFAULT_EXTENSIONS = [".txt", ".csv"]


class TheyreEatingHer(RuntimeError):
    """
    A poorly acted exception.
    """
    pass


class ThenTheyreGoingToEatMe(RuntimeError):     #Changed the ?paramater? of the class so it did not call the other class and cause a bug
    """
    A more specific poorly acted exception.
    """
    pass


def troll_check(text):
    """
    Returns a copy of the string `text` with the substring 'goblin' replaced
    with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

    Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
    Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in
        `text`, and the substring 'troll' is not found in `text`.
    """

    text = text.replace("hobgoblin", "orc").replace("goblin", "elf")  #Moved the replace function up here in case 'raise' ends the function and added 'text ='
                                                                      #as well as switching the replace functions around to fix the bug
    if "troll" in text:
        raise TheyreEatingHer("Best line ever.")

    elif "Nilbog" in text:    #Changed if to elif
        raise ThenTheyreGoingToEatMe("Oh my ...")   #gooooooooooooooooooooooood

    #text.replace("goblin", "elf").replace("hobgoblin", "orc")

    return text    #Returned text


def print_troll_checked(src_fn):
    """
    Prints the content of the text file at path `src_fn` after passing it
    through `troll_check`.

    Returns 0 if neither a 'troll', nor a 'Nilbog' was found.
    Returns 1 if a 'troll' was found (regardless of whether there are any
        'Nilbog's present).
    Returns -1 if no 'troll' was found, but a 'Nilbog' was found. (A 'Nilbog'
        is a negative troll for some reason. Don't think about it too much.)
    """
    try:
        with open(src_fn) as f: text = f.read()     #modified to use a with / as context manager, thanks Corey!
    except FileNotFoundError: return 0

    try:
        print(troll_check(text))
        #return 0

    except TheyreEatingHer:
        print("We found trolls!")
        return 1

    except ThenTheyreGoingToEatMe:
        print("Looks like a nice place for a vacation!")
        return -1

    else: return 0     #added an else and moved return 0 down here because I heard that was best practice or something


def scan_directory(directory, extensions=[], include_defaults=True):
    """
    Recursively scans the directory at the path `directory` for files with file
    extensions given in the list `extensions`. If `include_defaults` is True,
    the file extensions [".txt", ".csv"] are included in the search.

    Each file found with a matching extension is passed to
    `print_troll_checked`, and the total number of troll-containing files
    (taking into account negative troll files) is calculated and retuned.
    """

    print("Opening the laptop, the expresso tasted great!.")

    if include_defaults is True:  #Added 'is True' just incase 
        extensions += DEFAULT_EXTENSIONS

    number_of_troll_files = 0
    for root, dirs, files in os.walk(directory):
        for fn in files:
            temp = "." + fn.split(".")[1]   #modified to include the '.' at the beginning 
            if temp in extensions:
            #if ("." + fn.split(".")[1]) in extensions:
                ret = print_troll_checked(root + "/" + fn)   #added root + '/'
                number_of_troll_files += ret     #Indented this line of code

    print(f"Scanning complete. Found {number_of_troll_files} trolls.") #Modified to use an f-string instead. I like f-strings
    return number_of_troll_files