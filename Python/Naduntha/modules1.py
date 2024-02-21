# import random

# x = 0
# x = random.randint(1,100)
# print(x)

import random
import os

x = random.randint(1,10)
guess = int(input("enter a value: "))
print("correct asw : " , x)

if guess == x:
    print("you win")
else:
    os.remove("")

    # pip install pyinstaller
    # how to install qt designer on linux