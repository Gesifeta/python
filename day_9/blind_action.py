from art import logo
continue_bidding ='y'
bid_list ={}

print(logo)
def blind_bid():
    # TODO-1: Ask the user for input
    name = input("Enter your name\n")
    price = int(input("Enter your bid\n"))
    # TODO-2: Save data into dictionary {name: price}
    bid_list[name] = price
    # TODO-3: Whether if new bids need to be added
    # TODO-4: Compare bids in dictionary

while continue_bidding.lower() != "n":
    blind_bid()
    continue_bidding = input("Would you like to add more bidders:")
winner =0
for bid in bid_list:
    if bid_list[bid] > winner:
        winner = bid_list[bid]
print("The winner is ",winner)
print("The bids are \n",bid_list)
