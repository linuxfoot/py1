#!/bin/bash
#File Name:e*.sh
#Created Time:Tue Aug  11 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#Note: nginx top 8 using shell array
#Key:
##########################################################################
clear
ru() {
declare -A ip
while read line
do
  let ip[$line]++
done<ip3.sh
for i in ${!ip[@]}
do
echo "${ip[$i]}:$i"
done
}
cou=(`ru|sort -r|head -n 8|awk '{print $1}'`)
for j in ${!cou[@]}
do
name=`echo ${cou[$j]}|awk -F ":" '{print $2}'`
count=`echo ${cou[$j]}|awk -F ":" '{print $1}'`
echo " RANK is $[$j+1] :  $name get [ $count ] times"
done
























