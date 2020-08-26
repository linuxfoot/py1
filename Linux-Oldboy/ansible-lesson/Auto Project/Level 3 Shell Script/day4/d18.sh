#!/bin/bash
#File Name:e*.sh
#Created Time:Tue Aug  11 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#Note:Jumpserver simulator
#Key:系统开机自动执行,显示主机列表，不能强行退出
##########################################################################
clear
menu() {
  cat <<eof
  ----------Jumpserver demo-------------
  host list:
  a.10.0.1.7
  b.10.0.1.51
  --------------------------------------
eof
}
while true
do
 menu
 read -p "Please input your number: " inp
 if [ $i ]