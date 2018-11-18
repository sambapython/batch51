'''
import sys
#sys.path.append("/home/khyaathi-python/Desktop")
sys.path.insert(1,"/home/khyaathi-python/Desktop")
print sys.path
import accounts
print accounts.a
print accounts.b
print accounts.c
accounts.fun()
'''
#import app
#from app import file1
#from app.file1 import fun
'''
import app
app.file2.fun()
'''
'''
from app import file2
file2.fun()
'''
'''
import app
app.file1.fun()
'''
from app import file2
file2.fun()