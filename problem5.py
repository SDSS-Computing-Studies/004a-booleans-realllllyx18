

#  In math, if a quadratic equation is in the format
# ax^2 + bx + c = 0, the discriminant can be calculated as
# b^2 - 4 * a * c
# If the discriminant is a perfect square, the equation can
# be factored.  Furthermore, if the discriminant is negative,
# then the equation has no solutions (not used in this assignment).
# Have the user enter in values for a, b and c and then 
# tell them if the equation can be factored.

# Inputs:
# - 3 numbers (a, b, c)

# Outputs:
# - "the equation can be factored"
# - "the equation can not be factored"

import math

a=input("Enter the number")
b=input("Enter the number")
c=input("Enter the number")

result=(float(b)**float(2))-(float(4)*float(a)*float(c))
result=float(result)

if result==0:
    print("the equation can be factored")
else:
    print("the equation can not be factored")
