#!/bin/sh
count=`awk -F'[ :]+' '{++S[$NF]} END {for (key in S) print key,S[key]}' /etc/passwd`
echo $count
