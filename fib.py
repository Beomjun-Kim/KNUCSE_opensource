#!/usr/bin/python


n = int(raw_input("How much to do fibonacci?"))
if(n<1):
    print "It should be bigger than 1"
    exit(1)

prev = 0
new_sum = 1
temp = 0

for i in range(0,n-1,1):
    temp = new_sum
    new_sum = prev + new_sum
    prev = temp

print(new_sum)
