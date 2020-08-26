#!/bin/bash
#File Name:b.sh
#Created Time:Thu Aug  6 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
##########################################################################
if [ $USER == "root" ];then
 echo "You are root!"
fi

if [ $UID == 0 ];then
  echo "You are root, too!"
fi

if [ $1 -eq $2 ];then
  echo "$1 = $2"
  elif [ $1 -gt $2 ];then
  echo "$1 > $2"
  else
    echo "$1 < $2"
fi


if [ $1 -ne $2 ];then
  if [ $1 -gt $2 ];then
    echo "$1 > $2"
    else
    echo "$1 < $2"
  fi
else
  echo "$1 = $2"
fi

