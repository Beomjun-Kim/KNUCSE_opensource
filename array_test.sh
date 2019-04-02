#!/bin/bash

declare -a arr
counter=0
flag=1

while [ $flag -eq 1 ]
do
    read -p "Enter a new word: " input

    if [ $input = "list" ]
        then
            echo ${arr[*]}
    elif [ $input = "quit" ]
        then
            exit 0
    else
        arr[$counter]=$input
        counter=$(($counter+1))
        echo "Length: $counter"
    fi
done
