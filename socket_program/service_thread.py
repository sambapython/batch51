"""
1.hostname, port: 
2.make url using port, hostname
need to wait for client request.
once it got the request, it has to accept that and process the request send response back
"""
import threading
import socket
import time
hostname = socket.gethostname()
port=8899
def process(soc):
	clientsocket.send("hello firfox how are you?")
	req_data = clientsocket.recv(10)
	try:
		time.sleep(10)
		resp = "EVEN" if int(req_data)%2==0 else "ODD"
	except Exception as err:
		resp = "expecting only digits, " + err.message
	clientsocket.send(resp)
try:
	s=socket.socket()
	s.bind(("10.0.2.15", port))
	while True:
		s.listen(200)
		print "service runnning in %s:%s"%(hostname, port)
		print "waiting for the client request"
		clientsocket, clientinfo = s.accept()
		process_thread = threading.Thread(target=process, args=(clientsocket,))
		process_thread.start()
except Exception as err:
	print err
finally:
	s.close()