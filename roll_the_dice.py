"""
Dice Rolling Simulator
User can choose the number of side the dice have.
And how many dice do they want to roll.
Also, they can try as many times they want.
"""
#! python3
import os
os.system('clear')
import time

def main():
    """Main function of the game."""
    #Roll the dice base on the number of side and dice the user has chosen.
    roll_dice(num_side(), num_dice())
    #Check if they want to roll again.
    try_again()

def num_side():
    """Check how many sides of dice do user want."""
    while True:
        sides = input("\nHow many sides of dice do your want? ")
        try:
            sides = int(sides)
            if sides > 0:
                return sides
            else:
                print("Plese enter a positive interger.")
        except ValueError:
            print("Please enter a positive interger.")

def num_dice():
    while True:
        dices = input("How many dice do you want to roll? ")
        try:
            dices = int(dices)
            if dices > 0:
                return dices
            else:
                print("Plese enter a positive interger.")
        except ValueError:
            print("Please enter a positive interger.")

def roll_dice(sides, dices):
    """Generate a random number based on user's input."""
    from random import randint

    result = []
    print("\nRolling dice...")
    for dice in range(0,dices):
        dice = str(randint(1,sides))
        result.append(dice)
    time.sleep(0.5)
    if dices == 1:
        print("The result is " + result.pop() + ".")
    else:
        print("The result are " + ", ".join(result) + ".")

def try_again():
    """Check if the user want to play again."""
    while True:
        again = input("\nDo you want to roll again? (y/n): ")
        again = again.lower()
        if again == "y":
            return main()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Sorry, this is not a valid answer.")
            continue

"""Run the programme."""
if __name__ == "__main__":
    #Greet the user
    print(":::Python mini game - Rolling dice:::")
    #Run the programe.
    main()