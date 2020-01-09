import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 1337)
client_socket.connect(server_addr)
msg = "Message to send as a string"
client_socket.send(bytes(msg,'utf8'))