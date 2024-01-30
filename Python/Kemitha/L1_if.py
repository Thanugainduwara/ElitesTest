x = int(input("Enter Your Marks:"))
if x>101 and x>=0:
    if x>=75:
        print("A")
    elif x>=65:
        print("B")
    elif x>=55:
        print("C")
    elif x>=35:
        print("S")
    else :
        print("Fail")
else:
    print("invalid marks")
