print "program started."
import time
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
print "before conversion a=%s, b=%s"%(a,b)
try:
    a=float(a)
    b=float(b)
    time.sleep(10)
    print "after conversion a=%s, b=%s"%(a,b)
    res=a/b
    print "result=%s"%(res)
except ZeroDivisionError as err:
    print err
    print "dont eter zero for b"
except ValueError as err:
    print err
    print "expecting only digits"
except Exception as err:
    print "Error message:",err
except:
    print "some issue from your system end.."
print "main after except"
print "other statements in program"
print "program ended."