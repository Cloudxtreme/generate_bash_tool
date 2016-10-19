#!/bin/sh

IP=`ifconfig eth0 | awk -F '[ :]+' 'NR==2 {print $4}'`
echo  $IP
