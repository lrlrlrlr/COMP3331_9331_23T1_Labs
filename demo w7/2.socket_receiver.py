import socket
import atexit


server_address = ('127.0.0.1', 10086)
receiver_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
receiver_socket.bind(server_address)

# close socket when exit
def close_socket():
    receiver_socket.close()
atexit.register(close_socket)


while True:
    incoming_msg = receiver_socket.recvfrom(1024)
    if incoming_msg:
        print(incoming_msg)
