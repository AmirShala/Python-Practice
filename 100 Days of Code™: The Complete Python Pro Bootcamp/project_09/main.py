"""
Secret Auction Program – Documentation
=====================================

Overview
--------
This script simulates a secret auction where users submit bids.
At the end, the program determines and displays the highest bidder.

Features
--------
- Collects multiple bids using a loop
- Stores bids in a dictionary (name → bid amount)
- Identifies the highest bidder
- Clears screen between bidders (simple spacing)

Function
--------
- find_highest_bidder(bidding_record):
  Iterates through all bids and finds the highest one,
  then prints the winner and their bid.

Program Flow
------------
1. Display logo
2. Repeatedly ask for:
   - bidder name
   - bid amount
3. Store each bid in a dictionary
4. Ask if more bidders exist:
   - "yes" → continue
   - "no" → determine winner
5. Print the highest bidder

Example
-------
Input:
    Alice → 100
    Bob → 150

Output:
    The winner is Bob with a bid of $150

"""


from art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
