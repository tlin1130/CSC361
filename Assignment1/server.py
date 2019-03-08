from socket import *
import sys 
import codecs

serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:

    #establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 
            
    try:
        message = connectionSocket.recv(1024).decode()               
        filename = message.split()[1]                 
        f = codecs.open(filename[1:],'r')
        outputdata = f.read()

        #Send one HTTP status line into socket
        statusline = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(statusline.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        message = 'HTTP/1.1 404 Not Found\r\n'
        connectionSocket.send(message.encode())

        #close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #terminate the program after sending the corresponding data
