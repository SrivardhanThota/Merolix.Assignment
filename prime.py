#Write a function that checks if a given number is prime.

def prime(number):
  s="Number is Prime"
  for i in range(2,number):
    if number %i!=0:
      continue
      
    else:
      s= "Number is not Prime"
      break
  print(s)
      
number=int(input("enter the number"))
prime(number)