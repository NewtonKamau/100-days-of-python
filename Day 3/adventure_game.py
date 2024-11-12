print("Welcome to the Treasure Island.\n Your mission is to find the treasure.")
side = input("which side do you want to go? right or left \n")
lower_side =side.lower()
if(side =="right"):
    print("Game Over.")
else:
    swim = input("would you like to swim or wait \n")
    if(swim =="swim"):
        print("Game over.")
    else:
        door = input("which door color would you want to go in? blue, red or yellow \n")
        if(door =="yellow"):
            print("you win")
        else:
            print("Game over.")