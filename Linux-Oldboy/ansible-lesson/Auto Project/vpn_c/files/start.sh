#!/bin/bash
cd /etc/openvpn
nohup /usr/sbin/openvpn /etc/openvpn/client/client.conf > /dev/null &