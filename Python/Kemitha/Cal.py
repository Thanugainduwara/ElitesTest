#Function to perform addition operation
def add(a, b):
    return a + b

# Function to perform subtraction operation
def subtract(a, b):
    return a - b

# Function to perform multiplication operation
def multiply(a, b):
    return a * b

# Function to perform division operation
def divide(a, b):
    print( a / b)
#calculator
def calculator():
    while True:
        print("Select operation.")
        print("1.Add      : +")
        print("2.Subtract : -")
        print("3.Multiply : *")
        print("4.Divide   : /")
        print("ctrl + c to exit")
        choice = input(str("Enter choice(+,-,*,/): "))
        print ("Your Choice Is :",choice)

        if choice not in ["+", "-", "*", "/","^","%"]:
            print("Invalid choice. Please try again.")
            continue

        # Get inputs from user
        a = int(input("Enter first number: "))
        print(a)
        b = int(input("Enter second number: "))
        print(b)
        
        if choice == "+":
            result = add(a, b)
            print(a,"+",b,"=", result)
        elif choice == "-":
            result = subtract(a, b)
            print(a,"-",b,"=", result)
        elif choice == "*":
            result = multiply(a, b)
            print(a,"*",b,"=", result)
        elif choice == "/":
            result = divide(a, b)
            print((a,"/",b,"="),result)
            
calculator()