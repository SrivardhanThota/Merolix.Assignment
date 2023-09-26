# 8.Implement a simple menu-driven program in Python. Ask the user to choose an option from a menu 
#(e.g., 1 for "Calculate Area," 2 for "Calculate Perimeter," 3 for "Exit").
# Depending on their choice, perform the corresponding action or exit the program.

menu=["Calculate Area", "Calculate Perimeter", "Exit"]
choosedoption=int(input("Choose your option:"))
print(menu[choosedoption-1])