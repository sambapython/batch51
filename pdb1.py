print "program started"
a=10
b=20
c=a+b
print a,b,c
def fun(x,y):
	print x,y
	try:
		z=x+y
		z1=x-y
		return z,z1
	except Exception as err:
		print err
print "some statements"
import pdb; pdb.set_trace()
for i in [1,2,0,3,4]:
	print i
	if i!=0:
		print 10/i
fun(100,200)
print "some other statements"
print "program ended"