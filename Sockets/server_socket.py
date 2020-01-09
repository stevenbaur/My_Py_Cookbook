import socket                                                       #importiere sockets

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #definiere einen socket AF_INET = ipV4, SOCK_STREAM = TCP
server_socket.bind(('127.0.0.1', 1337))                             #Auf welche Adresse soll der Server hören? (bei Internet-server empfiehlt sich gethostname() )
server_socket.listen(1)                                             #starte das Hören für n clients (bei mehr als 1 unbedingt Threading nutzen!)

while True:                                                         #Dauerschleife, in der der Server läuft
    (client_socket, addr) = server_socket.accept()                  #Verbindung vom Client akzeptieren
    msg = str(client_socket.recv(512),'utf8')                       #Empfange die Nachricht und konvertiere Bytes zurück in String
                                                                    #recv(Buffergröße)
    print(msg)                                                      #Zeige die Nachricht an.
                                                                    #Bei komplexeren Themen empfiehlt es sich, dass der jeweilige client(thread) eine Klasse erzeugt,
                                                                    #die wiederum die gewünschten Aufgaben erfüllt