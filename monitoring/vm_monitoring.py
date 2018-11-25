from server import connect
from db import get_con
class VM:
	def __init__(self, username, password, ip):
		self.user=username
		self.pwd=password
		self.host_ip=ip 
	def connect(self):
		server=connect()
		con_vm = server
		return con_vm
	def get_temp(self):
		con_vm = self.connect()
		# code to get a temparature
	def inert(self):
		con,cur = get_con()
		cur.execute("insert into(id,username,password,ip) values(1,'%s','%s','%s')"%(self.user,
			self.password,self.ip))

		
