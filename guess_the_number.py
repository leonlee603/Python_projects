"""
This is a programme where the computer randomly generates a number between 0 and 20. 
The user needs to guess what the number is. 
If the user guesses wrong, tell them their guess is either too high, or too low. 
If the user get the right number, tell them how many times they have tried.
"""
#! python3
from random import randint
import os
os.system('clear')

def main():
    """This is the main programme to get the number from user and check the answer."""
    #Generate a random number between 0 and 20.
    ans = randint(0,20)
    #Create a variable to count the number of trial.
    num_try = 0
    
    while True:
        guess = input("\nPlease enter a number: ")
        
        try:
            if int(guess) == ans:
                num_try += 1
                print("Correct! you've got the right number " + str(guess) + "!")
                if num_try == 1:
                    print("You have tried only " + str(num_try) + " time!")
                else:
                    print("You have tried " + str(num_try) + " times.")
                return play_again()
            elif int(guess) > ans and int(guess) <= 20:
                num_try += 1
                print("Your number is larger than the answer.")
            elif int(guess) < ans and int(guess) >= 0:
                num_try += 1
                print("Your number is small than the answer.")
            elif int(guess) < 0 or int(guess) > 20:
                print("Your answer can only be an positive integer between 0 to 20.")
        except ValueError:
            if guess.lower() == "quit" or guess.lower() == "q":
                print("Thanks for playing! See you!")
                break
            else:
                print("Your answer can only be an positive integer between 0 to 20.")

        
def play_again():
    """To see if the user want to play it again."""
    while True:
        again = input("\nDo you want to play again? (y/n): ")
        if again.lower() == "y":
            return main()
        elif again.lower() == "n" or again.lower() == "quit" or again.lower() == "q":
            print("Thanks for playing! See you!")
            break
        else:
            print("Please enter 'y'/'n'.")
            continue

def greeting():
    """Greeting that will only show once on the top of the game."""
    print("Welcome to the number guessig game.")
    print("Try to guess a number between 0 to 20!")
    print("(Enter 'quit'/'q' anytime to exit.)")

#Call the function and start the game.
if __name__ == "__main__":
    greeting()
    main()