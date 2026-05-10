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
# Function to get user preferences for password generation
def get_preferences():
    print(" Select character types to include in your password:")
    include_uppercase = get_yes_no(" Include uppercase letters?")
    include_lowercase = get_yes_no(" Include lowercase letters?")
    include_digits = get_yes_no(" Include digits?")
    include_symbols = get_yes_no(" Include symbols?")
    
    if not any([include_uppercase, include_lowercase, include_digits, include_symbols]):
        print(" ⚠ You must select at least one character type.")
        return get_preferences()
    
    return {
        'uppercase': include_uppercase,
        'lowercase': include_lowercase,
        'digits': include_digits,
        'symbols': include_symbols
    }
# Function to build character sets based on user preferences
def build_char_set(preferences):
    char_set = ""
    if preferences['uppercase']:
        char_set += UPPERCASE
    if preferences['lowercase']:
        char_set += LOWERCASE
    if preferences['digits']:
        char_set += DIGITS
    if preferences['symbols']:
        char_set += SYMBOLS
    return char_set
# Function to gaurantee requirements are met
def generate_password(length, char_set, preferences):
    password = []
    if preferences['uppercase']:
        password.append(random.choice(UPPERCASE))
    if preferences['lowercase']:
        password.append(random.choice(LOWERCASE))
    if preferences['digits']:
        password.append(random.choice(DIGITS))
    if preferences['symbols']:
        password.append(random.choice(SYMBOLS))
    
    while len(password) < length:
        password.append(random.choice(char_set))
    
    random.shuffle(password)
    return ''.join(password)
# Check password strength
def check_strength(password):
    strength = "Weak"
    if (any(c in UPPERCASE for c in password) and
        any(c in LOWERCASE for c in password) and
        any(c in DIGITS for c in password) and
        any(c in SYMBOLS for c in password) and
        len(password) >= 12):
        strength = "Strong"
    elif (any(c in UPPERCASE for c in password) and
          any(c in LOWERCASE for c in password) and
          any(c in DIGITS for c in password) and
          len(password) >= 8):
        strength = "Moderate"
    return strength
# function to display password and strength
def display_password(password):
    strength = check_strength(password)
    print("\n Generated Password:")
    print(f" {password}  ({strength})")

# Function to save password to file using os module to get desktop path
def save_password(password):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "generated_password.txt")

    try:
        os.makedirs(desktop_path, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(password)
        print(f" Password saved to: {file_path}")
    except OSError:
        file_path = os.path.join(os.path.expanduser("~"), "generated_password.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(password)
        print(f" Desktop not found. Password saved to: {file_path}")

# Main function to control program flow
def main():
    print("\n ╔═══════════════════════════╗")
    print(" ║ PASSWORD GENERATOR         ║")
    print(" ║ Phase 1 — Python          ║")
    print(" ╚═══════════════════════════╝")
    
    length = get_length()
    preferences = get_preferences()
    char_set = build_char_set(preferences)
    password = generate_password(length, char_set, preferences)
    display_password(password)
    
    if get_yes_no("\n Do you want to save the password to a file?"):
        save_password(password)
        print(" Goodbye! Keep coding. 👋")

# Entry point
if __name__ == "__main__":
    main()