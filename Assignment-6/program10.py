"""10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
a,b,c=input("first number ..:"),input("second number...:"),input("third number...:")
if(a==b)and(b==c):
    print(a,b,c,"are equal number.")
elif(a>b)and (b>c):{
    print(a,"is greatest number.")
}
elif(b>a) and (b>c):
    print(b,"is greatest number.")
else:
    print(c,"is greatest number.")      
