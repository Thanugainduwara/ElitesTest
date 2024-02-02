sub=["sinhla","english","maths","ICT","science"]
marks=[]
for i in range(len(sub)):
    userinput=int(input("enter marks for "+sub[i]+": "))
    marks.append(userinput)
print()
for i in range(len(sub)):
    print("Your marks for",sub[i],"is",marks[i])