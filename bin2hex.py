#!/src/bin/python

binum=input("Please enter a number: ")
str1=str(binum)
len1=len(str1)
hex1=0;
bin1=0
mul=1
hex_num=[1,2,3,4,5]
index_cnt = 0
cnt=0

for i in range(len1-1,-1,-1):
    if str1[i]=="0":
        bin1=0*mul
    elif str1[i]=="1":
        bin1=1*mul
    hex1=hex1+bin1
    cnt=cnt+1
    mul=mul*2
    if (cnt%16==0 or i==0):
        hex_num[index_cnt]=hex1
        index_cnt=index_cnt+1
        hex1=0
        mul=1
        
for i in range(index_cnt-1,-1,-1):
    print "%.04X"% int(hex_num[i]),
