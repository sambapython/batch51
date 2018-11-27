import socket
hostname="khyaathipython"
port=8899
try:
	s=socket.socket()
	s.connect(("10.0.2.15", port))
	ack = s.recv(1024)
	print "acknowledgement:",ack
	data = raw_input("Enter a number:")
	s.send(data)
	resp = s.recv(1024)
	print "response: ",resp
except Exception as err:
	print err
finally:
	s.close()