import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length: "))
    complexity = int(input("Enter the complexity level (1/2/3): "))

    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)

except ValueError:
    print("Please enter valid inputs.")
