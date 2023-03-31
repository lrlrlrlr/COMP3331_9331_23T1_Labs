import threading
import time
import logging, sys
logging.basicConfig(
    # filename="Receiver_log.txt",
    stream=sys.stderr,
    level=logging.DEBUG,
    format='%(asctime)s,%(msecs)03d [%(threadName)s] %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S')

def print_message(n=10):
    for i in range(n):
        logging.debug(i)
        time.sleep(1)


# print_message(20)
t1 = threading.Thread(target=print_message)
t2 = threading.Thread(target=print_message, args=(20,))

t1.start()
t2.start()

# t1.join()
# t2.join()