import os

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux, macOS, and other POSIX systems
        os.system('clear')


bidder_details = {}

while True:
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid?\n"))  # cast to int
    bidder_details[name] = bid

    another_bidder = input("Is there another bidder? (yes/no)\n").strip().lower()
    if another_bidder == "yes":
        clear_screen()
    elif another_bidder == "no":
        break
    else:
        print("Invalid input, assuming no more bidders.")
        break

# Find the highest bidder
winner_name = max(bidder_details, key=bidder_details.get)
highest_bid = bidder_details[winner_name]

print(f"The winner is {winner_name} with a bid of ${highest_bid}")
