#!/bin/sh

NTP_TIME=`/usr/sbin/ntpdate 1.cn.pool.ntp.org`

echo $NTP_TIME
