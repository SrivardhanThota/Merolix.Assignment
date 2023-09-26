# 4. Create a Python program that asks the user for their exam score (0-100) and prints "A" if the score is 90 or above, "B" 
#if it's between 80 and 89, "C" if it's between 70 and 79, "D" if it's between 60 and 69, and "F" if it's below 60.

Examscore=int(input("Enter Your Marks"))

if Examscore>=90 and Examscore<=100:
    print("The grade is A")

elif Examscore>=80 and Examscore<=90:
    print("The Grade is B")

elif Examscore>=70 and Examscore<=80:
    print("The Grade is c")

elif Examscore>=60 and Examscore<=70:
    print("The Grade is D")

else:
    print("F (Failed)")