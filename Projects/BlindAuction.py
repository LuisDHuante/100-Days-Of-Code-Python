import os 
logo = '''
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

bids = {}
bidding_finished = False

def find_highest_bidder(bids):
    fin_max = max(bids, key=bids.get)
    print(f"The winner is {fin_max} with a bid of ${bids.get(fin_max)}")

while not bidding_finished:
    os.system ("cls")
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Y or 'N'.\n")
    if should_continue == "N":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Y":
        os.system ("cls")
  