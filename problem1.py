#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

number=input("Enter a number")
number=float(number)

if number%2 == 0:
    print("the number is even")
if number%2 > 0:
    print("the number is odd")
