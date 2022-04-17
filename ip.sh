#!/bin/bash

# modified from: https://shumeipai.nxez.com/2020/01/02/send-email-raspberry-pi-ip-with-python.html

wlan0=`/sbin/ifconfig  wlan0 | head -n2 | grep inet | awk '{print$2}' `
eth0=`/sbin/ifconfig  eth0 | head -n2 | grep inet | awk '{print$2}'`
gee=`/usr/bin/python3 /home/pi/updateIP/getIP.py 2> /home/pi/updateIP/getIP.err`

if ping -c 2 -W 3 www.baidu.com &> /dev/null ;then
/usr/bin/curl "https://[USERNAME]:[PASSWORD]@freedns.afraid.org/nic/update?hostname=[DOMAIN]&myip=$gee" &> /home/pi/updateIP/FreeDNS.log
#/home/pi/updateIP/mail.py another@email.com  "Reporting Raspberry Pi IP $gee" "wlan0: $wlan0 || eth0: $eth0 || gee: $gee" # send IP by emil, if no domain
fi
