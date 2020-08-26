#!/bin/bash
#File Name:e*.sh
#Created Time:Tue Aug  11 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#Note: array basic
#Key:
##########################################################################
clear
book[0]=MacOS
echo "book 0 is "${book[0]}
book=(linux windows)
echo "book 0 is "${book[0]}
echo "book all are "${book[@]}
echo "book index are "${!book[@]}
echo "book size is "${#book[@]}
declare -A info
info=([name]=names [age]=a)
echo ${info[name]}
result=($(ls))
echo "members are: "${result[@]}





















