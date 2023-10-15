import math

# Function to perform addition
def add():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(f"{x} + {y} = {x+y}")

# Function to perform subtraction
def subtract():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(f"{x} - {y} = {x-y}")

# Function to perform multiplication
def multiply():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f"{x} * {y} = {x*y}")

# Function to perform division
def divide():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if y == 0:
        return "Cannot divide by zero"
    print(f"{x} / {y} = {x/y}")

# Function to calculate the power
def power():
    x = int(input("Enter the Base number: "))
    y = float(input("Enter the Power number: "))
    print(f"{x} power {y} = {x**y}")

# Function to calculate square root
def square_root():
    x = float(input("Enter the number: "))
    if x < 0:
        return "Cannot calculate square root of a negative number"
    return print(f"Sqrt of {x} = {math.sqrt(x)}")

# Function to calculate remainder
def remainder():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if y == 0:
        return "Cannot calculate remainder when the divisor is zero"
    print(f"{x} % {y} = {x%y}")


status = True

print("Simple Calculator :\n")
print("Choose an operation:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. Remainder")
print("8. Exit")

while status:
    try:
        
        choice = int(input("Enter operation choice (1/2/3/4/5/6/7/8): "))

        if choice not in (1, 2, 3, 4, 5, 6, 7, 8):
            print("Invalid choice")

        else:

            if choice == 1:
                add()

            elif choice == 2:
                subtract()

            elif choice == 3:
                multiply()

            elif choice == 4:
                divide()
                
            elif choice == 5:
                power()
                
            elif choice == 6:
                square_root()
                
            elif choice == 7:
                remainder()

            elif choice == 8:
                print("Thankyou")
                status = False

    except ValueError:
        print("Invalid input. Please enter valid numbers.")