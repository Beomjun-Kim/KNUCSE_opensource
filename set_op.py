#!/usr/bin/python

var1=raw_input("Please enter the first list: ")
var2=raw_input("Please enter the second list: ")

no_space1=var1.replace(" ","")
no_space1=no_space1.replace("[","")
no_space1=no_space1.replace("]","")
no_space2=var2.replace(" ","")
no_space2=no_space2.replace("[","")
no_space2=no_space2.replace("]","")

list1=no_space1.split(",")
list2=no_space2.split(",")

print(list1[0])

len1=len(list1)
len2=len(list2)

union=[]
intersect=[]

for i in range(0,len1):
    union.append(int(list1[i]))
for i in range(0,len2):
    if int(list2[i]) not in union:
        union.append(int(list2[i]))

for i in range(0,len1):
    for j in range(0,len2):
        if list1[i]==list2[j]:
            if int(list1[i]) not in intersect:
                intersect.append(int(list1[i]))


print "Union: ",union
print "Intersection: ",intersect
