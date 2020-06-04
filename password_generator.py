"""
:::Password Generator:::
This is a programme which generates a random password for the user. 
Ask the user how long they want their password to be.
Then the programme will generate a password with a mix of upper and 
lowercase letters, as well as numbers and symbols. 
The password should be a minimum of 8 characters long which contain at
least two of each type of character.
"""
#! python3
from random import choice, shuffle, randint
import string
import os
os.system("clear")

def main():
    """The main body of the programme."""
    #Get the length of the password from user.
    length = length_pw()
    #Generate the password with user's designed length.
    pw = gen_pw(length)
    #Randomly change the order of the password generated.
    shuffle(pw)
    #Show the generated password to user.
    print("Your password is: " + "".join(pw))
    #Check if they want to generate another password again.
    try_again()

def gen_pw(length):
    """Generate a password and save it in a list."""
    #Creating variable for 8 characters password.
    #Make sure the password contain at least 2 of each type of character.
    upper_case_letter_1 = choice(string.ascii_uppercase)
    upper_case_letter_2 = choice(string.ascii_uppercase)
    lower_case_letter_1 = choice(string.ascii_lowercase)
    lower_case_letter_2 = choice(string.ascii_lowercase)
    number_1 = choice(string.digits)
    number_2 = choice(string.digits)
    symbol_1 = choice(string.punctuation)
    symbol_2 = choice(string.punctuation)
    #Creat a list to store the password.
    password = [
        upper_case_letter_1,
        upper_case_letter_2,
        lower_case_letter_1,
        lower_case_letter_2,
        number_1,
        number_2,
        symbol_1,
        symbol_2,
    ]
    if length == 8:
        #If user want a password with 8 characters.
        return password
    else:
        #If user want a password more than 8 characters.
        #Add the extra characters with random type of characters.
        extra_index = length - 8
        for extra_pw in range(0,extra_index):
            random_type = randint(0,3)
            if random_type == 0:
                extra_pw = choice(string.ascii_uppercase)
                password.append(extra_pw)
            elif random_type == 1:
                extra_pw = choice(string.ascii_lowercase)
                password.append(extra_pw)
            elif random_type == 2:
                extra_pw = choice(string.digits)
                password.append(extra_pw)
            elif random_type == 3:
                extra_pw = choice(string.punctuation)
                password.append(extra_pw)
        return password

def shuffle_pw(password):
    """Shuffle the password generated as a list by gen_pw()."""
    shuffle(password)
    return password

def length_pw():
    """Get the length of password that user wants."""
    while True:
        message = "\nHow many characters do you want as a password? "
        length = input(message)
        try:
            length = int(length)
        except ValueError:
            print("[Invaild input] Please enter a positive interger larger than or equal to 8.")
            continue
        else:
            if length <=7:
                print("[Invaild input] Please enter a positive interger larger than or equal to 8.")
                continue
            else:
                return length

def greeting():
    """Display the basic information that only shows once when the programme start."""
    print("This is a Password Generator")
    print("I can generate a random password of 8 or more characters for you.")
    print("In order to createu a strong password, ")
    print("each password will contain and mix the following elements:")
    print("- at least 2 uppercase letters from A to Z")
    print("- at least 2 lowercase letters from a to z")
    print("- at least 2 digits from 0 to 9")
    print("- at least 2 punctuation signs such as !,?,',# etc")
    print("Let's start creating password!")

def try_again():
    while True:
        again = input("\nDo you want to genetate another password? (y/n): ")
        if again.lower() == "y":
            return main()
        elif again.lower() == "n":
            print("See you next time!")
            break
        else:
            print("[Invaild input] Please enter y/n.")
            continue

#Run the programme.
if __name__ == "__main__":
    greeting()
    main()
