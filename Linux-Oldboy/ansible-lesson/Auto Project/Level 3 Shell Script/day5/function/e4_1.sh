#!/bin/bash
#File Name:e*.sh
#Created Time:Tue Aug  11 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#Note: file = $1 使用return返回 && ||
#Key:
##########################################################################
clear
getfile() {
  if [ -f $1 ];then
    return 0
    else
      return 1
  fi
}

getfile $1
jud=$?
if [ $jud -eq 0 ];then
  echo "File $1 is existed."
  else
    echo "File $1 no found."
fi























