#!/bin/bash
. /etc/init.d/functions

for ip in `cat ip.txt`
do
	expect ssh-copy-id -i /root/.ssh/id_dsa.pub $ip >/dev/null 2>&1

	if [ -eq 0 ];then
		action "$ip" /bin/true
	else	
		action "$ip" /bin/false
	fi
done
