#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    path = '/home/wtc/problems/submission_001-hangman/short_words.txt'
    words_file = open(path, 'r')
    global listvar
    listvar = words_file.readlines()
    return [] 


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    i = random.randint(0,20)
    words = listvar[i]
    strlen = len(words) - 2
    x = random.randint(0,strlen)
    l = words[x]
    temp = words.replace(l , '_' , 1)

    print(temp)
    return words


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    user_ans = input("Guess the missing letter:")

    return 'TODO'


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')
