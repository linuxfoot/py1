#!/bin/bash
#File Name:c.sh
#Created Time:Thu Aug  7 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#case with nginx
##########################################################################
clear
source /etc/init.d/functions
cat <<eof
-----Nginx controller------
1.Start
2.Stop
3.Restart
4.Status
5.Quit
eof
read -p "Please input your choice: " choice
status=$(pidof nginx|wc -l)
case $choice in
1)
  if [ $status -eq 0 ];then
    nginx
    sleep 1
    action "nginx started, pid is $(pidof nginx)" /bin/true
    exit
    else
      action "nginx already started. No more action." /bin/false
  fi
;;
2)
  if [ $status -eq 0 ];then
    action "Nginx not found, no more action." /bin/false
    exit
    else
      nginx -s stop
      sleep 1
      status=$(pidof nginx|wc -l)
      if [ $status -eq 0 ];then
        action "Stopped successfully" /bin/true
        exit
        else
          action "Stopped failed" /bin/false
      fi
  fi
;;
4)
  if [ $status -eq 0 ];then
        action "Nginx not found" /bin/false
        exit
        else
         action "Nginx started, pid is $(pidof nginx)" /bin/true
  fi
;;
3)
  if [ $status -eq 0 ];then
        action "Nginx not found, please start it using 1." /bin/false
        exit
        else
         nginx -s reload
         sleep 1
         action "Nginx REstarted, pid is $(pidof nginx)" /bin/true
  fi
;;
*)
  echo "Bye."
  exit
esac