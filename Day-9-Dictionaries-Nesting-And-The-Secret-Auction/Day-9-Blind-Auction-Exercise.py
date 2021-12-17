from Art import logo
import os

print(logo)

bid_dict = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    another_bid = input("Any other bidders? yes or no \n")
    if another_bid == "no":
        bidding_finished = True
        find_highest_bidder(bid_dict)
    elif another_bid == "yes":
        clear()
        