subjects=["sinhala","english","maths","ict","music"]
marks=[]

for i in range(len(subjects)):
    mark = int(input("Enter the mark for "+subjects[i]+": "))
    marks.append(mark)

for i in range(len(subjects)):
    print(subjects[i]+" : "+str(marks[i]))