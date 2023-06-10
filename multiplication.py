""" times table"""
Z = (int(input("please enter a value whose table you want to create       ")))
if Z == 0:
    print("you have entered a zero")
else:
    for x in range (1,11):
        print (f"{Z}*{x} = {x * Z}")
print("thank you")


#second method
X = int(input("Please input a value for the times table"))
Y= 1
while Y <= 15:
    if X>=1:
        print(f"{X}*{Y}={X*Y}")
        Y+=1
    else:
        print("you have entered an invalid number")
print("thank you")
