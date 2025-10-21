# What does the game do?

# intro
# dictionaries are presented in key, value pairs

# compare values from different dictionaries in a list
# If position A is empty, place a dictionary in this position
# Pull a dictionary from the list and place this one in position B
# Compare
# use A and B, when correct, the highest score moves to A
# if wrong, game over and display correct count
# create A function that returns the follower count from a dictionary
# create a function that compares the follower count of A and B
# create a function that keeps looping as long the answer is correct

# A new comparison is presented.
# Use a random function to pull a dictionary from the list.
# place this dictionary in position B
# compare this one with A

import random
import game_data
from game_data import data

#variables
dictionary_A = 0
dictionary_B = 0
follower_count = 0
answer_is_correct = True

#create a function that compares A and B and replaces B when equal to A
# def replace_B_when_equal_to_A(A,B):
#     while A == B:
#         dictionary_B = select_random_dictionary()
#         B = follower_count
#         return B
#
# replace_B_when_equal_to_A(A_count,B_count)

def select_random_dictionary():
    """create a function that can randomly pull an item from the list"""
    selected_dictionary = random.choice(data)
    return selected_dictionary

def follower_count(dictionary):
    """A function that returns the follower count from a dictionary"""
    follower_count = int(dictionary["follower_count"])
    return follower_count

# def compare(A_number_followers,B_number_followers,choice):
#     """A function that compares the follower count of A and B """
#     if A_number_followers > B_number_followers and choice == "A":
#         print(f"you're correct")
#     elif A_number_followers < B_number_followers and choice == "B":
#         print(f"You're correct")
#     else:
#         print(f"You're wrong")

# create a function that keeps looping as long the answer is correct
def loop_while_correct(A_number_followers,B_number_followers,choice):
    while answer_is_correct == True:
        #players_choice = input(f"Who has more followers A or B ?")
        if A_number_followers > B_number_followers and choice == "A":
            print(f"you're correct")

        elif A_number_followers < B_number_followers and choice == "B":
            print(f"You're correct")
        else:
            print(f"You're wrong")
            answer_is_correct = False
    else:
        print("game over")

dictionary_A = select_random_dictionary()
dictionary_B = select_random_dictionary()
A_count = follower_count(dictionary_A)
B_count = follower_count(dictionary_B)


print(f"A = {dictionary_A}")
print(f"B = {dictionary_B}")
players_choice = input(f"Who has more followers A or B ?")
print(A_count)
print(B_count)

loop_while_correct(A_count,B_count,players_choice)


#compare(A_count,B_count,players_choice)
#
#
#
# if follower_count == 0:
#     select_random_dictionary()
#     follower_count = follower_count()
#
# elif:
