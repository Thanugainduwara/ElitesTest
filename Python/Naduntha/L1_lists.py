'''
list1 = [100,"Hello",True,3.14]

for i in list1:
    print(i)
else :
    print("NO Iems left")    



# append() Function
list01 = [5 , 10 , 15 , 20 , 25 , 30]
list01 .append(35)
print(list01)


# insert() function
list01 = [5 , 10 , 15 , 20 , 25 , 30]
list01 .insert(5,29)
print(list01)


# pop() function
list01 = [5 , 10 , 15 , 20 , 25 , 30]
list01 .pop()
print(list01)

# remove() function
list01 = [5 , 10 , 15 , 20 , 25 , 30]
list01 .remove(15)
print(list01)

list01 = [5 , 10 , 15 , 20 , 15 , 25 , 30]
list01 .remove(15)
print(list01)

# len() function
list01 = [5 , 10 , 15 , 20 , 15 , 25 , 30]
print(len(list01))

# accessing item using index 
list01 = [5 , 10 , 15 , 20 , 15 , 25 , 30]
list01[5] = 0
print(list01)
'''
# printing list using for loop 
list01 = [5 , 10 , 15 , 20 , 25 , 30]
for i in range(len(list01)):
    print(list01[i])

