#Write a Python function to calculate the factorial of a non-negative integer.
n=int(input("Enter the number"))
def factorial(k):
    s=1
    if k>1:
        s=k*factorial(k-1)
    return s
    
result=factorial(n)
print(result)