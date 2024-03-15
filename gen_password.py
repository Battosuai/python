import string
import random

characters = string.ascii_letters

digits = string.digits

symbols = string.punctuation

try:
    password_length = int(input("Your password length?\n"))

    password = ""

    for i in range(0, password_length):
        if i == 0:
            password += random.choice(characters)
        else:
            randomOption = random.randint(1, 3)
            if randomOption == 1:
                password += random.choice(characters)
            elif randomOption == 2:
                password += random.choice(digits)
            elif randomOption == 3:
                password += random.choice(symbols)

    print(f"Your password: {password}")
except ValueError:
    print("You have to give a number")
