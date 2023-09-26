# 2. Create a Python program that asks the user for their age. If the age is less than 18, it should print "You are a minor." If the age is between 18 and 65, it should print "You are an adult."
#If the age is 65 or older, it should print "You are a senior citizen.

age=int(input("Enter the Age"))
if age<18:
    print("You are a minor.")  #age is below 18 so Minor
elif age>=65:
    print("You are a Senior Citizen.") #if your age is greaterthan or equals to 65 then Adult
else:
    print("You are an Adult") 