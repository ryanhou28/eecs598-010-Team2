#!/bin/bash
times=100
echo > f
for (( c=0; c<$times; c++ ))
do 
   python3 delay_line_memory_look_up_table.py
done
echo "run programs for $times times"
echo "correct times: " 
grep -o success f | wc -l
echo "times"
