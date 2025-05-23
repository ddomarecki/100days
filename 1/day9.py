import os
def find_highest_bidders(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")



bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is ur name?: ")
    price = int(input("What is ur bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidders(bids)
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')



