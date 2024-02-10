Subjects= ["Sinhala","Maths","ICT","Science","Commerce"]
marks =[]
for i in range (len(Subjects)):
    mark = int(input("Enter the mark for "+Subjects[i]+" :"))
    marks.append(mark)

for i in range( len(Subjects)):
    print(Subjects[i]+" : "+str(marks[i]))
 
 



