import random


def code_generator(): 
    """This function generates the code"""
    
    global code
    code = [0,0,0,0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value    #This is where the code is generated

def get_user_input(): 
    return input("Input 4 digit code: ")


def code_check(answer): 
    """Compares the user input to the code and calculates the output to 
    present to the user"""

    answer = list(answer)
    correct_digits_and_position = 0
    correct_digits_only = 0

    for i in range(len(answer)): #This is where the check begins
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1 #This is where the check ends.

    return correct_digits_and_position, correct_digits_only

def display_code():
    """Displays the code to the user at the end of the game"""
    
    print("The code was: " + str(code))

# TODO: Decompose into functions
def run_game():
    """Handles the function calls and output"""
    code_generator()
    print(code)  #Julian left this in the code so I'm assuming it's important
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_user_input()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue

        correct_digits_and_position, correct_digits_only = code_check(answer)
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
    
    display_code()
    

if __name__ == "__main__":
    run_game()
