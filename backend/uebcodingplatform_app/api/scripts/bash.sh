!/bin/bash
start=$(date -u +%s%N)
output=""

javac -d classes $2

compiler_result=$?

if [ $compiler_result -eq 0 ]
then
  output=$(echo $1 | java $2)
fi

end=$(date -u +%s%N)
time=$((($end-$start)/1000000))
sed -i -r "s/^(TIME=).*/\1$(echo $time)/" env.txt
sed -i -r "s/^(OUTPUT=).*/\1$(echo $output)/" env.txt
sed -i -r "s/^(COMPILER_RESULT=).*/\1$(echo $compiler_result)/" env.txt