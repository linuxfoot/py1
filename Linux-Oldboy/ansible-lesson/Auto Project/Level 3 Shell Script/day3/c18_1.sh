#!/bin/bash
#File Name:c.sh
#Created Time:Fri Aug  7 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#通过读入文件中的用户与密码文件，进行批量添加用户。文件中的格式: user:passwd
##########################################################################
clear
total=`awk 'END{print NR}' profile.txt`
for num in `seq 1 $total`
do
  pre=`awk -F ":" -v no=$num 'NR==no{print $1}' profile.txt`
  pass=`awk -F ":" -v no=$num 'NR==no{print $2}' profile.txt`
  id $pre &>/dev/null
  jud=$?
  if [ $jud -eq 0 ];then
    echo "user $pre existed, no more action"
    else
      useradd $pre &>/dev/null
      echo $pass | passwd --stdin $pre &>/dev/null
      echo "user $pre created successfully."
      echo "Password is " $pass
  fi
done