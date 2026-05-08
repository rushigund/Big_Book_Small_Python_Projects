'''
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
'''
import random 

MAX_ATTEMPT = 10 #max number of attempt user can have

def get_secret_number():
    "creating random number to guess"
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_number = ""
    for i in range(3):
        secret_number += str(numbers[i])
    
    return secret_number

def get_clues(user_input,secret_number):
    if user_input == secret_number:
        return "you got it"

    clues = []

    for i in range(len(user_input)):
        if user_input[i] == secret_number[i]:
            clues.append("Ferni")
        elif user_input[i] in secret_number:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    
    else:
        clues.sort()
        return " ".join(clues)

def main():

    print(
    '''
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it.
    '''
    )

    while True:
        attempt_number = 1
        random_number = get_secret_number()
        print("I have a number in my mind")
        print(f"you can make guesses upto {MAX_ATTEMPT}")

        while(attempt_number<MAX_ATTEMPT):
            print(random_number)
            user_input = input(f"Guess #{attempt_number}")

            clues = get_clues(user_input,random_number)
            print(clues)
            attempt_number += 1

            if user_input == random_number:
                print("correct")
                break
            else:
                print("incorrect")
                print("try again")

        print("Do you want to continue type:y / type anything for negative response ")   
        if not input('> ').lower().startswith('y'):
            break
    

if __name__== '__main__':
    main()

