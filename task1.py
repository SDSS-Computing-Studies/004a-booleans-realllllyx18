#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"

number=input("Enter a number")

number=float(number)

if number>100:
    print("the number is larger than 100")
if number<100:
    print("the number is smaller than 100")
if number==100:
    print("the number is 100")
