import logging
logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s==>%(levelname)s=>%(message)s",
    filename="log.txt")
logging.info("program started.")
a=raw_input("Enter a value:")
b=raw_input("Enter b value:")
logging.debug("before conversion a=%s, b=%s"%(a,b))
try:
    a=float(a)
    b=float(b)
    logging.debug("after conversion a=%s, b=%s"%(a,b))
    res=a/b
    print "result=%s"%(res)
    logging.debug("result=%s"%(res))
except ZeroDivisionError as err:
    logging.error(err.message)
    print "dont eter zero for b"
    logging.error("dont eter zero for b")
except ValueError as err:
    logging.error(err.message)
    print "expecting only digits"
    logging.error("expecting only digits")
except Exception as err:
    print "Error message:",err
    logging.error("%s"%err.message)
logging.info("main after except")
logging.info("other statements in program")
logging.info("program ended.")