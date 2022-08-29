"""12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

x=complex(input("Enter  comlex number ..:"))
print("real part of complex number is ..:",x.real)
print("imaginary part of complex is ...:",x.imag)
if(x.real>x.imag):
    print(x.real,"is greater than imaginary part.")
else:
    print(x.imag,"is greater than real part.")   