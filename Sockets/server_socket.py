import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 1337))
server_socket.listen(1)

while True:
    (client_socket, addr) = server_socket.accept()
    msg = str(client_socket.recv(512),'utf8')
    print(msg)