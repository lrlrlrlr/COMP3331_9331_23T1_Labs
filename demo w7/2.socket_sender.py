import socket
import atexit


server_address = ('127.0.0.1', 12345)
destination_address = ('127.0.0.1', 10086)


sender_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sender_socket.bind(server_address)

# close socket when exit
def close_socket():
    sender_socket.close()
atexit.register(close_socket)


# send message
message = b"msg"
sender_socket.sendto(message,destination_address)
