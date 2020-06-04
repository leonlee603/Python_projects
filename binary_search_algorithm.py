"""
Create a random sorted list of numbers between 0 and 100. 
Ask the user for a number between 0 and 100 to check whether 
their number is in the list. The programme should work like this. 
The programme will half the list of numbers and see whether the users 
number matches the middle element in the list. If they do not match, the 
programme will check which half the number lies in, and eliminate the other 
half. The search then continues on the remaining half, again checking 
whether the middle element in that half is equal to the user’s number. 
This process keeps on going until the programme finds the users number, 
or until the size of the subarray is 0, which means the users number 
isn't in the list.
"""
#! python3
from random import randint
import os
os.system('clear')

def main():
    """Programme's main body."""
    #Generate a random list.
    list_nums = gen_list()
    #Get the input from user.
    user_num = get_user_num()
    #Check the input using binary search.
    result = binary_search(list_nums, user_num)
    #Print the result.
    telling_result(result)
    #Check if try again.
    try_again()

def gen_list():
    """Generate a random sorted list."""
    list_nums = []
    while len(list_nums) < 50:
        num = randint(0,100)
        if num in list_nums:
            continue
        else:
            list_nums.append(num)
    list_nums.sort()
    return list_nums

def get_user_num():
    """Get the number from user."""
    while True:
        message = "\nPlease enter a number between 0 - 100,"
        message += " and I'll check if it is in the list. "
        user_num = input(message)
        try:
            user_num = int(user_num)
            if user_num < 0 or user_num > 100:
                print(str(user_num) + " isn't an interger between 0 - 100.")
            else:
                return user_num
        except ValueError:
            print(user_num + " isn't an interger between 0 - 100. ")
           
def binary_search(list, item):
    """Do the binary search to check the user's number."""
    lower_index = 0
    upper_index = len(list) - 1
    while lower_index <= upper_index:
        mid_index = (lower_index + upper_index)//2
        check = list[mid_index]
        if check == item:
            return item
        elif check > item:
            upper_index = mid_index - 1
            continue
        elif check < item:
            lower_index = mid_index + 1
            continue
    return None

def telling_result(result):
    """Print the result of the binary search."""
    if result:
        print("\nYes! Your number is in the list.")
    else:
        print("\nSorry, your number isn't in the list.")

def try_again():
    """Check if user want to try the programme again."""
    while True:
        again = input("\nDo you want to try again? (y/n) ")
        if again.lower() == "y":
            return main()
        elif again.lower() == "n":
            print("Thanks for trying! See you!")
            break
        else:
            print(again + " is not a valid input.")
        

#Run the programme.
if __name__ == "__main__":
    main()