"""
login,
set resources for thest
test the resouce
delete the resource
logout
"""
import unittest
from app import fun
class FunTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "this is log in"
		cls.user="user1"

	@classmethod
	def tearDownClass(cls):
		print "logout"
		cls.user=None
	def setUp(self):
		print "setting the resource"
	def tearDown(self):
	 	print "deleting the resource"

	def test_fun_10_20(self):
		#print "setting the resource"
		print self.user
		exp=30
		act=fun(10,20)
		self.assertEqual(exp,act,"test_fun_10_20 failed")
		#print "deleting the resource"
	def test_fun_s1_s2(self):
		#print self.user
		exp="s1s2"
		act=fun("s1","s2")
		self.assertEqual(exp,act,"test_fun_s1_s2 failed")
		#print "deleting the resource"
	def test_fun_s1_20(self):
		#print "setting the resource"
		print self.user
		exp=None
		act=fun("s1",20)
		self.assertEqual(act,exp,"test_fun_s1_10 failed")
		#print "deleting the resource"
	def test_fun_10_s2(self):
		#print "setting the resource"
		print self.user
		exp=None
		act=fun(10,"s2")
		self.assertEqual(act,exp,"test_fun_10_s2 is failed")
		#print "deleting the resource"
#unittest.main()