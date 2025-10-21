
#HINT: You can call clear() to clear the output in the console.

from art import hammer
print(hammer)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("Welcome to the auction bidder.")

more_bidders = input("Are there any more bidders? Yes or no?")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("what is your bid?"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)  #calls the previously defined function(find_highest_bidder) and passes in the bids




