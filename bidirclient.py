import socket
cli=socket.socket()
cli.connect(('127.0.0.1',1090))
message=raw_input(" -> ")
while message!= 'q' :
	cli.send(message)
	data = cli.recv(1024)
	print('Received from server: ' + data)
	message = raw_input("->")
cli.close()
