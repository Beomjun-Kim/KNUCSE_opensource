#!/usr/bin/python

n = int(raw_input("How much to do fibonacci?"))

prev = 0
new_sum = 1
temp = 0

for i in range(0,n-1,1):
    temp = new_sum
    new_sum = prev + new_sum
    prev = temp

print(new_sum)
