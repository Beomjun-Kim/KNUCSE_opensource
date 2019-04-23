#!/usr/bin/python
import sys

fname=sys.argv[1]
word_num=int(sys.argv[2])

with open(fname,'r') as f:
    text = f.read()
    word_list=text.split()

word_list_no_dup = list(set(word_list))
word_count = []

for word in word_list_no_dup:
    word_count.append((word_list.count(word),word))

n=0

for result in sorted(word_count, reverse=True):
    n=n+1
    print "%-10s %10d"%(result[1],result[0])
    if n==int(sys.argv[2]):
        break
