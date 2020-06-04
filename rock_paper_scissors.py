"""
This is a rock-paper-scissors game which allow player vs the computer. 
The computer’s answer will be randomly generated, 
while the program will ask the user for their input. 
"""

from random import randint
import os
os.system('clear')

def main():
    """This is the main programme to get the choice from user and compare with the 
    computer's choice which generated randomly."""
    while True:
        message = "\nPaper, scissors, rock!!"
        message += "\n1.)Paper\n2.)Scissors\n3.)Rock"
        message += "\nLet's make your choice. (1/2/3): "
        user_choice = input(message)
        computer_choice = randint(1,3)

        if user_choice == "1":
            if computer_choice == 1:
                print("\nYou choose paper and computer chooses paper too.")
                print("It's a draw.")
            elif computer_choice == 2:
                print("\nYou choose paper and computer chooses scissors.")
                print("You lose!")
            elif computer_choice == 3:
                print("\nYou choose paper and computer chooses rock.")
                print("You win!")
            play_again()
            break
                
        elif user_choice == "2":
            if computer_choice == 1:
                print("\nYou choose scissors and computer chooses paper.")
                print("You win!")
            elif computer_choice == 2:
                print("\nYou choose scissors and computer chooses scissors too.")
                print("It's a draw.")
            elif computer_choice == 3:
                print("\nYou choose scissors and computer chooses rock.")
                print("You lose!")
            play_again()
            break

        elif user_choice == "3":
            if computer_choice == 1:
                print("\nYou choose rock and computer chooses paper.")
                print("You lose!")
            elif computer_choice == 2:
                print("\nYou choose rock and computer chooses scissors.")
                print("You win!")
            elif computer_choice == 3:
                print("\nYou choose rock and computer chooses rock too.")
                print("It's a draw.")
            play_again()
            break

        elif user_choice.lower() == "q" or user_choice == "quit":
            print("\nThanks for playing! See you!")
            break
            
        elif user_choice != 1 or 2 or 3:
            print("\nInvalid input. Please try again.")

def greeting():
    """Greeting that will only show once on the top of the game."""
    print("Welcome to the 'Paper, scissors, rock' game!!")
    print("(Enter 'quit'/'q' anytime to exit.)")

def play_again():
    """To see if the user want to play it again."""
    while True:
        again = input("\nDo you want to play again? (y/n): ")
        if again.lower() == "y":
            return main()
        elif again.lower() == "n" or again.lower() == "quit" or again.lower() == "q":
            print("\nThanks for playing! See you!")
            break
        else:
            print("Please enter 'y'/'n'.")
            continue

#Call the function and start the game.
if __name__ == "__main__":
    greeting()
    main()