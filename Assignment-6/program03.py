#3. Write a python script to check whether a given number is even or odd

# x=int(input("Enter any number to check it's number even or odd...:"))
# if(x%2==0) : print("it is even number .")
# else : print("it is odd number.")

x=int(input("Enter any number to check it's number even or odd...:"))
if(x&1) : print("it is odd number.")
else : print("it is even number .")
