import socket
s=socket.socket()
port=input("enter port no")
s.connect(('127.0.0.2',port))
while (1):
	msg=s.recv(1024)
	if (msg=='q'):
		break
	else:
		print msg
