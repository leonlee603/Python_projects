import random
from words import word_list
import os
os.system("clear")
#! python3

def main():
    """A funtion that run the whole programme."""
    #Generate a random word from word list.
    word = get_word()
    #Run the game.
    play(word)
    #Check if user want to play again.
    try_again()

def get_word():
    """Randomly select a word in the word_list.py"""
    word = random.choice(word_list)
    return word.upper()

def play(word):
    """Main body of the hangman project."""
    #Set a flag for while loop.
    guessed = False
    #Lists for storing the guessed item.
    guessed_letters_wrong = []
    guessed_letters_correct = []
    guessed_words = []
    tries = 6
    
    #Initial information on screen.
    print("Welcome to the python mini game - Hangman!")
    print(display_hangman(tries))
    #List for showing the guessing word on screen.
    word_as_list = []
    for i in range(0,len(word)):
        i = "_"
        word_as_list.append(i)
    word_completion = " ".join(word_as_list)
    print(word_completion)
    print("\n")
    
    #While loop for user's input and compare the guess with word.
    while tries > 0 and guessed == False:
        previous_guess_correct = ",".join(guessed_letters_correct)
        previous_guess_wrong = ",".join(guessed_letters_wrong)
        print("Previous Guesses(letters in the word) : " + previous_guess_correct)
        print("Previous Guesses(letters not in the word): " + previous_guess_wrong )
        guess = input("Please guess a letter or word: ").upper()
        #Situation of guessing a letter.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters_correct:
                print("You already guessed the letter " + guess + ".")
            elif guess in guessed_letters_wrong:
                print("You already guessed the letter " + guess + ".")
            elif guess not in word:
                print(guess + " is not in the word.")
                tries -= 1
                guessed_letters_wrong.append(guess)
            else:
                print("Good job, " + guess + " is in the word")
                guessed_letters_correct.append(guess)
                #Find out the location of guess in word.
                indices = []
                for i, letter in enumerate(word):
                    if letter == guess:
                        indices.append(i)
                #Relpace each underscore at index with guess.
                for index in indices:
                    word_as_list[index] = guess
                if "_" not in word_as_list:
                    guessed = True
                
        #Situation of guessing a word.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word " + guess + ".")
            elif guess != word:
                print(guess + " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            elif guess == word:
                guessed = True
        #Situation of invalid input.
        else:
            print("This is not a valid guess.")
        
        #Repeat for next letter.
        print(display_hangman(tries))
        word_completion = " ".join(word_as_list)
        print(word_completion)
        print("\n")

    #Print the result after while loop shop.
    if guessed == True:
        print("Congrats, you guessed the word! You win.")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time.")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def try_again():
    """Check if user want to play again."""
    while True:
        again = input("Do you want to play it again?(y/n): ")
        again = again.lower()
        if again == "y":
            return main()
        elif again == "n":
            print("Thanks for playing! See you!")
            break
        else:
            print("This is not a valid input.")
            continue


if __name__ == "__main__":
    main()
