import socket

#Creating the socket object
serverSocket = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
)

host = socket.gethostbyname()
port = 3000

#Binding to the socket
serverSocket.bind((host, port)) #Host will be replaced/substitued with IP. if changed and not running on host

#Starting ICP listener
serverSocket.listen(3)

while True:
    #Starting the connection
    clientScoket, adress = serverSocket.accept()

    print("Received conncetion from " % str(adress))

    message = 'Hei, Thanks for connecting to server' + "\r\n"
    clientScoket.send(message)

    clientScoket.close()