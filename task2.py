#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

number=input("Enter a number")

number=float(number)

if number>0:
    print("The number is positive")
if number<0:
    print("The number is negative")
if number==0:
    print("The number is zero")
