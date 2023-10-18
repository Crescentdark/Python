from replit import clear
#Made in replit
#HINT: You can call clear() to clear the output in the console.
from Excerssises.art import logo
print(logo)

bids = {}
bidding_finished = False

def find_high_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_am = bidding_record[bidder]
    if bid_am > highest_bid:
      highest_bid = bid_am
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


  
while not bidding_finished:
  name = input("What is your name " )
  price = int(input("What is your bid? $ "))
  bids[name] = price
  should_cont = input("Are there any other bidders? Type 'yes' or 'no' ")
  if should_cont == "no":
    bidding_finished = True
    find_high_bidder(bids)
  elif should_cont == "yes":
    clear()
    