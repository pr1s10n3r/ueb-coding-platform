#!/bin/bash
start=$(date -u +%s%N)
output=$(printf $1 | java $2)
end=$(date -u +%s%N)
time=$((($end-$start)/1000000))
sed -i -r "s/^(TIME=).*/\1$time/" env.txt
sed -i -r "s/^(OUTPUT=).*/\1$(echo $output)/" env.txt
