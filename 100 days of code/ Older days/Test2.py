import random



#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    """a function that draws a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randomNumber = random.randint(0, 12)
    randomcard = cards[randomNumber]
    return randomcard

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(drawn_cards):
    """Take a lists of cards and return the score calculated from the cards"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
    # 0 will represent a blackjack in our game.
    if sum (drawn_cards) == 21 and len == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to look up append() and remove().
    if 11 in drawn_cards and sum(drawn_cards) > 21:
        drawn_cards.remove(11)
        drawn_cards.append(1)
    return sum(drawn_cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score,
# then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21,
# then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins"
    elif user_score == 0:
        return "You win"
    elif user_score > 21:
        return "You loose"
    elif computer_score > 21:
        return "Computer loses"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    # The underscore is there for to let the range function run, but we are not interested to giving it a name.

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        #this is the same just shorter
        computer_cards.append(deal_card())


    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards : {user_cards}, Your score = {user_score}")
        print(f" Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function
        # to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("Do you want another card? press 'y' or 'n' ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    # != means not equal to zero
    while (computer_score < 17 and computer_score != 0):
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input(f"Do you want to play a game of blackjack? 'y' or 'n' ") == "y":
    play_game()
