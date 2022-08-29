"""4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""
x=int(input("Enter first number to check which is greater..:"))
y=int(input("Enter second number to check which is greater..:"))
if x != y:
    if (x>y) : 
     print(x,"is greatest number ")
    else: 
     print(y,"is greatest number ")
else :
    print(x,"and",y,"are equal ")




