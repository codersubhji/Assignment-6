#9. Write a python script to check whether a given year is a leap year or not.
x=int(input("Enter any year ...:"))
if(x%400==0) or (x%4==0) and (x%100 !=0):
    print(x," is leap year.")
else:
    print(x," is not leap year.")      