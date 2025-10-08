# even_odd.py
# Program to check whether a number is even or odd

# Step 1: Take integer input from user
number = int(input("Enter an integer: "))

# Step 2: Check if even or odd using if-else
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
