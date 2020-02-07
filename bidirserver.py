import socket
ser=socket.socket()
ser.bind(("127.0.0.1",1090))
ser.listen(2)
con,addr=ser.accept()
print("connection from:" + str(addr))
while True:
	data=con.recv(1024)
	if not data:
		break
	print("from connected user:" + str(data))
	data = raw_input('->')
	con.send(data)
con.close()
