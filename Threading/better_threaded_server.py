import socket
import sys

host = ''
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)

def threaded_c(conn):
    conn.send(str.encode('Welcome, type your info\n'))

    while True:
        data = conn.recv(1024)
        reply = 'Server output: ' + data.decode(data,'utf8')
        if not data:
            break
        conn.sendall(str.encode(reply))
