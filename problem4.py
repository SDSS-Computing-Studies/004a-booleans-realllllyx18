
#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

a=input("Enter a number")
b=input("Enter a number")
c=input("Enter a number")
if float(a)+float(b)>float(c):
    if float(a)+float(c)>float(b):
        if float(b)+float(c)>float(a):
            if float(a)**float(2)+float(b)**float(2)==float(c)**float(2):
                print("that is a right triangle")
            if float(a)**float(2)+float(b)**float(2)>float(c)**float(2):
                print("that is an obtuse triangle")
            if float(a)**float(2)+float(b)**float(2)<float(c)**float(2):
                print("that is an acute triangle")
