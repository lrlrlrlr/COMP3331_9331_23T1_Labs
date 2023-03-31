import logging, sys

logging.basicConfig(
    # filename="Receiver_log.txt",
    stream=sys.stderr,
    level=logging.WARNING,
    format='%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S')

logging.debug("hi!")
logging.warning("warning!")