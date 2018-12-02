import logging
logging.basicConfig(level=logging.DEBUG,
	format="%(asctime)s==>%(levelname)s=>%(message)s",
	filename="log.txt")
logging.warn("warning messages")
logging.info("info messages")
logging.error("error messages")
logging.debug("debug message")