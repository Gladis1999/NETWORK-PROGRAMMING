import socket
s=socket.socket()
port=input("enter port no")
c=input("enter no of clients ")
s.bind(('127.0.0.2',port))
s.listen(c)
i=1
con=[0 for i in range(c)]
addr=[0 for i in range(c)]
for i in range(c):
	con[i],addr[i]=s.accept()
while(1):
	msg=raw_input("enter message\n")
	for i in range(c):
		con[i].send(msg)
	if (msg=="q"):
		break

s.close()
