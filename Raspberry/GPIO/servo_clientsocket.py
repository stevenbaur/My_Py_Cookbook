import socket                                                       #importiere sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #definiere einen socket AF_INET = ipV4, SOCK_STREAM = TCP

server_addr = ('192.168.178.129', 1337)                                   #Adresse des Servers als Tupel (IP,PORT)
client_socket.connect(server_addr)                                  #Verbinde zum Server
msg = str(input("Grad angeben: "))                                                          #Zu übertragende Nachricht
client_socket.send(bytes(msg,'utf8'))                               #Nachricht wird übertragen (es werden immer bytes übertragen!)
client_socket.close()