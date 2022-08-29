"""8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
a,b,c=int(input("Enter number..:")),int(input("Enter number..:")),int(input("Enter number..:"))
d=b**2-4*a*c
if d>0:
    print("Real and distinct roots")
elif (d==0):
    print("Real  and equals")  
else:
    print("Imaginary roots")      