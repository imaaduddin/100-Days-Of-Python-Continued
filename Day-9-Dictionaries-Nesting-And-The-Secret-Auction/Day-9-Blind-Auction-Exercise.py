from Art import logo
import os

print(logo)

bid_dict = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    bid = input("What is your bid? $")
    bid_dict[name] = bid
    another_bid = input("Any other bidders? yes or no")
    if another_bid == "no":
        bidding_finished = True
    else:
        