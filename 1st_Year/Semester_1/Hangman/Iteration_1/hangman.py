#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """

    read_file = open(file_name, 'r')
    words = read_file.readlines()
    return words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    i = random.randint(0,20)
    word = words[i]
    strlen = len(word) - 2
    x = random.randint(0 , strlen)
    l = word[x]
    temp = word.replace(l , '_' , 1)

    print("Guess the word:", temp)
    return word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    answer = input("Guess the missing letter: ")

    return answer


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
