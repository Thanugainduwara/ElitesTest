# 2024/02/02
'''
# Quection 01 
num = int(input("Enter a POsitive Number"))

while num >= 0:
    print(num)
    num = int(input("Enter a POsitive Number"))
else : 
    print("You entered a negative number ") 
'''
# Quection 02
subject = ["sinhala" , "maths" , "english" , "ict"] 
marks =[]

for i in range(len(subject)):
    mark = int(input("Enter marks for " +subject[i]+": "))
    marks.append(mark)

for i in range(len(subject)):
    print(subject[i] + " : " +str(marks[i]))    