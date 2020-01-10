import threading
import socket
import time

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 1337))
    server_socket.listen(1)

    while True:
        (client_socket, addr) = server_socket.accept()
        msg = str(client_socket.recv(512),'utf8')
        print(msg)

def do_something():
    for _ in range(1000):
        print("doing something else while server is running..")

thread_one = threading.Thread(target=run_server)
thread_one.start()

for _ in range(5):
    do_something()