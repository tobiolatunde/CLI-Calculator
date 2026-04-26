# Import Random Module
import random
# Import String Module
import string
# Import OS module
import os
# Define character set constants
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation
# Input Function to get password length from user
def get_length():
    while True:
        try:
            length = int(input(" Enter desired password length (8-128): "))
            if 8 <= length <= 128:
                return length
            else:
                print(" ⚠ Please enter a number between 8 and 128.")
        except ValueError:
            print(" ⚠ Invalid input. Please enter a number.")
            
# Input Function To get Yes or No Answer from user
def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        print(" ⚠ Please enter 'y' for yes or 'n' for no.")