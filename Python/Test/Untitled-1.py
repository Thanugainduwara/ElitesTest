#Inputs two integer values. If the first is less than the second, print the message “up”. If the second is less than the first, print the message “down”. If the numbers are equal, print the message “equal”.

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if(x<y):
    print("up")
elif(y<x):
    print("down")
else:
    print("equal")
    