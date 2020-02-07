import socket
s=socket.socket()
s.bind(('127.0.0.1',1234))
s.listen(5)
con,addr=s.accept()
while(1):
	msg=raw_input("enter message\n")
	con.send(msg)
	if (msg=="q"):
		break
con.close()
		
