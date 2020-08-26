#!/bin/bash
#File Name:back00c.sh
#Created Time:Sun Jun 21 05:05:07 2020
#Author: Lzj
#mail: harry_lee2683@outlook.com
##########################################################################
pathk="/root/backup/`hostname`-`hostname -i`/"
pathk1="`hostname`-`hostname -i`/"
timek=`date -d "-1 day" "+%F-%a-%T"`
export RSYNC_PASSWORD=123456
mkdir $pathk -p
cd /
tar zcf ${pathk}sys_bak_${timek}.tar.gz etc/passwd
find $pathk -mtime +7 -delete
cd $pathk
cd ..
find $pathk1 -mmin -1 -name '*gz'|xargs md5sum >${pathk1}finger.txt
rsync -avLz $pathk rsync_backup@autobak::bak-all/`hostname`-`hostname -i`