#Task
"""
Divisible By Ten

Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False




Coding question

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.
"""


# Define the function divisible_by_ten
def divisible_by_ten(num):
    # Check if the remainder when num is divided by 10 is 0
    if num % 10 == 0:
        return True
    else:
        return False

# Ask the user for input
num = int(input("Enter a number: "))

# Call the function and print the result
if divisible_by_ten(num):
    print(f"{num} is divisible by 10: True")
else:
    print(f"{num} is not divisible by 10: False")
