import os
from art import logo
clear = lambda: os.system('cls')
clear()
print(logo)
should_continue = True
bidders = {}
def highest_bidder(bidders_dic):
    highest = 0
    for key in bidders_dic :
        if bidders_dic[key] > highest :
            highest = bidders_dic[key]
            winner_name = key
    print(f"The winner is {winner_name} with a bid of ${highest}")
    
while should_continue : 
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bidder = input("Are there are other bidders ? Type 'yes' or 'no'.\n")

    if other_bidder == 'yes':
        clear()
    elif other_bidder == 'no' :
        should_continue = False
        clear()
        highest_bidder(bidders)




















