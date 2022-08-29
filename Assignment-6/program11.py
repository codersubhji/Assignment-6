"""11. Write a python script to take the month value in numeric format and display the
number of days in it."""
a=int(input("Enter any month value between 1 to 12..:"))
if(a==2):
    print("28 or 29 days")
elif a in (1,3,5,7,9,11,12):
    print("31 days") 
elif a in (4,6,8,10):
    print("30 days")  
else:
    print("Please enter valid digit between 1 to 12")       