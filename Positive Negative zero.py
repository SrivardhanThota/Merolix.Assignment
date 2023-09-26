# 3.Write a Python program that takes a number as input and prints "Positive" if it's greater than zero, "Negative" if it's less than zero, and "Zero" if it's equal to zero.

Number=int(input("Enter the Number"))
if Number>0:
    print("positive")
elif Number<0:
    print("Negative")
else:
    print("Zero")