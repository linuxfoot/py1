#!/bin/bash
#File Name:c.sh
#Created Time:Thu Aug  7 09:11:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
#case with php status
##########################################################################
clear
source /etc/init.d/functions
cat <<eof
-------- php status monitor -----
1.accepted
2.listen queue
3.max listen queue
4.listen queue len
5.idle processes
6.active processes
7.total processes
8.max active processes
9.max children reached
10.ALL
11.Quit
---------------------------------
eof
read -p "Please input your choice: " choice
systemctl status php-fpm &>/dev/null
live_fpm=$?
curl http://127.0.0.1:81/fpmstatus &>/dev/null
live_fpmstatus=$?
if [ $live_fpm -ne 0 ] || [ $live_fpmstatus -ne 0 ];then
  action "Please check php-fpm status." /bin/false
  exit
  else
    accepted=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==5{print $NF}'`
    listen_queue=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==6{print $NF}'`
    max_listen_queue=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==7{print $NF}'`
    listen_queue_len=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==8{print $NF}'`
    idle_processes=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==9{print $NF}'`
    active_processes=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==10{print $NF}'`
    total_processes=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==11{print $NF}'`
    max_active_processes=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==12{print $NF}'`
    max_children_reached=`curl -s http://127.0.0.1:81/fpmstatus | awk 'NR==13{print $NF}'`
    case $choice in
    1)
      echo "accepted=$accepted"
      ;;
    2)
      echo "listen_queue=$listen_queue"
      ;;
    3)
      echo "max_listen_queue=$max_listen_queue"
      ;;
    4)
      echo "listen_queue_len=$listen_queue_len"
      ;;
    5)
      echo "idle_processes=$idle_processes"
      ;;
    6)
      echo "active_processes=$active_processes"
      ;;
    7)
      echo "total_processes=$total_processes"
      ;;
    8)
      echo "max_active_processes=$max_active_processes"
      ;;
    9)
      echo "max_children_reached=$max_children_reached"
      ;;
    10)
      curl -s http://127.0.0.1:81/fpmstatus
      ;;
    *)
      echo "Bye."
      exit
    esac
fi
