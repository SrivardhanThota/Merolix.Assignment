''' 9. Create a Python program that categorizes people into age groups based on the following criteria:
0-12 years: Child
13-19 years: Teenager
20-59 years: Adult
60+ years: Senior Ask the user for their age and print their age group.
'''
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    age_group = "Teenager"
elif age >= 20 and age <= 59:
    age_group = "Adult"
else:
    age_group = "Senior"

print(f"You are in the {age_group} age group.")
