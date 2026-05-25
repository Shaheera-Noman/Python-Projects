from turtle import clear


logo = '''

    
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                       /_______________\
 '''              
import os
def clear_console():
 os.name == 'nt'
 os.system('cls')

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your Name?\n")
    price = input("What is your Bid?\n")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'. ")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
       clear_console()
