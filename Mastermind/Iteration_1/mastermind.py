import random


def run_game():
    
    code = [0, 0, 0, 0]
    index = 0

    while index < 4:
        x = random.randint(1, 8)
        if x not in code:
            code[index] = x
            index += 1
    code = "".join(map(str, code))

    guesses = 12
    print(code)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    user_in = input("Input 4 digit code: ")

    while list(user_in) != code and guesses != 1:
        if len(user_in) != 4 or user_in.isnumeric() == False:
            print("Please enter exactly 4 digits.")
            user_in = input("Input 4 digit code: ")
        range_check = ['0', '9']
        for x in user_in:
            if x in range_check:
                print("Please enter exactly 4 digits.")
                user_in = input("Input 4 digit code: ")
        else:
            temp = list(code)
            index = 0
            place_check = 0
            unit_check = 0

            while index < 4:
                if code[index] == user_in[index]: 
                    place_check += 1
                    temp[index] = '_'
                index += 1

            for x in user_in:
                if x in temp:
                    index = temp.index(x)
                    temp[index] = '_'
                    unit_check += 1

            print("Number of correct digits in correct place:    " , place_check)
            print("Number of correct digits not in correct place:" , unit_check)
            if place_check == 4:
                break
            guesses -= 1
            print("Turns left:" , guesses)
            user_in = input("Input 4 digit code: ")
    
    if guesses != 1: print("Congratulations! You are a codebreaker!")
    print("The code was:", "".join(code))


if __name__ == "__main__":
    run_game()
