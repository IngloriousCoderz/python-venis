import logging

logging.basicConfig(level=logging.ERROR, filename="example.log")

logging.debug("Debug message")
logging.info("Informational message")
logging.warning("Potential issues")
logging.error("An error occurred")
logging.critical("This is bad, shutting down")
