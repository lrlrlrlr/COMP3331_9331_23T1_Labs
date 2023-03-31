"""
    Sample code for Sender (multi-threading)
    Python 3
    Usage: python3 sender.py receiver_port sender_port FileToSend.txt max_recv_win rto
    coding: utf-8

    Notes:
        Try to run the server first with the command:
            python3 receiver_template.py 9000 10000 FileReceived.txt 1 1
        Then run the sender:
            python3 sender_template.py 10000 9000 FileToReceived.txt 1000 1

    Author: Rui Li (Tutor for COMP3331/9331)
"""
# here are the libs you may find it useful:
import datetime, time  # to calculate the time delta of packet transmission
import logging, sys  # to write the log
import socket  # Core lib, to send packet via UDP socket
from threading import Thread  # (Optional)threading will make the timer easily implemented

BUFFERSIZE = 1024


class Sender:
    def __init__(self, sender_port: int, receiver_port: int, filename: str, max_win: int, rot: int) -> None:
        '''
        The Sender will be able to connect the Receiver via UDP
        :param sender_port: the UDP port number to be used by the sender to send PTP segments to the receiver
        :param receiver_port: the UDP port number on which receiver is expecting to receive PTP segments from the sender
        :param filename: the name of the text file that must be transferred from sender to receiver using your reliable transport protocol.
        :param max_win: the maximum window size in bytes for the sender window.
        :param rot: the value of the retransmission timer in milliseconds. This should be an unsigned integer.
        '''
        self.sender_port = int(sender_port)
        self.receiver_port = int(receiver_port)
        self.sender_address = ("127.0.0.1", self.sender_port)
        self.receiver_address = ("127.0.0.1", self.receiver_port)

        # init the UDP socket
        logging.debug(f"The sender is using the address {self.sender_address}")
        self.sender_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.sender_socket.bind(self.sender_address)

        #  (Optional) start the listening sub-thread first
        self._is_active = True  # for the multi-threading
        listen_thread = Thread(target=self.listen)
        listen_thread.start()

        # todo add codes here
        pass

    def ptp_open_and_send(self):
        # todo add/modify codes here
        # send a greeting message to receiver
        # message = "Greetings! xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxCOMP3331."
        with open("random1.txt","rb") as file:
            content = file.read(1000)
        self.sender_socket.sendto(content, self.receiver_address)
        pass


    def ptp_close(self):
        # todo add codes here
        self._is_active = False  # close the sub-thread
        pass

    def listen(self):
        '''(Multithread is used)listen the response from receiver'''
        logging.debug("Sub-thread for listening is running")
        while self._is_active:
            # todo add socket
            incoming_message, _ = self.sender_socket.recvfrom(BUFFERSIZE)
            logging.info(f"received reply from receiver:, {incoming_message.decode('utf-8')}")

    def run(self):
        '''
        This function contain the main logic of the receiver
        '''
        # todo add/modify codes here
        self.ptp_open_and_send()
        self.ptp_send()
        self.ptp_close()


if __name__ == '__main__':
    # logging is useful for the log part: https://docs.python.org/3/library/logging.html
    logging.basicConfig(
        # filename="Sender_log.txt",
        stream=sys.stderr,
        level=logging.DEBUG,
        format='%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S')

    if len(sys.argv) != 6:
        print(
            "\n===== Error usage, python3 sender.py sender_port receiver_port FileReceived.txt max_win rot ======\n")
        exit(0)

    sender = Sender(*sys.argv[1:])
    sender.run()
