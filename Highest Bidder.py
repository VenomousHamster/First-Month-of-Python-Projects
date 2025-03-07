logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

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


auction_list = {}
continue_auction = True

while continue_auction:
    users_names = input("Please Enter Your Name.\n")
    users_bids = int(input("Now Enter Your Bid.\n"))
    auction_list[users_names] = users_bids
    user_choice = input("Is there another bid? Type Yes or No.\n").lower()
    print("\n" * 50)
    if user_choice == "no":
        continue_auction = False
        find_highest_bidder(auction_list)
