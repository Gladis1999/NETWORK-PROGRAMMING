import socket
s=socket.socket()
s.connect(('127.0.0.1',1234))
while(1):
	msg=s.recv(1234)
	if (msg=='q'):
	  	print msg
	  	break
	else:
	  	print msg
