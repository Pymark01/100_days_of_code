import random
import art
from art import hammer

def show_logo():
    print(hammer)

def random_number():
    '''A function for generating a random number'''
    randomnumber = random.randint(1,100 )
    return randomnumber

def select_difficulty():
    '''A function for selecting the difficulty'''
    difficulty = input("Choose a difficulty: 'easy' or 'hard'.")
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else :
        print("Choose a difficulty: 'easy' or 'hard'.")
    return attempts

randomnumber = random_number()
attempts = select_difficulty()
print(f"Number of attempts:{attempts}")
print(f"The number is : {randomnumber}")
def game():
    show_logo()
    for _ in range (attempts):
        guessed_number = int(input("Choose a number"))
        if guessed_number == randomnumber:
            print("You won")
            return
        # The return-command ends the function
        elif guessed_number > randomnumber:
            print("Too high, Try again.")
        elif guessed_number < randomnumber:
            print("Too low, Try again.")
        else:
            print("You loose.")
            return

#while input("Do you want to play the guessing game?" == "y"):
#    show_logo()
game()

