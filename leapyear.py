# 6. Create a Python program that checks if a given year is a leap year. 
#If the year is divisible by 4 but not divisible by 100, or it's divisible by 400, it's a leap year. Otherwise, it's not.

Year=int(input("enter Year"))
if Year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")