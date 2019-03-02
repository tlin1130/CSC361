from socket import *
import sys

serverIPAddress = sys.argv[1]
serverPort = sys.argv[2]
requestedFile = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIPAddress,int(serverPort)))

message = 'GET /' + requestedFile + ' HTTP/1.1\r\n'

clientSocket.send(message.encode())
response = clientSocket.recv(1024)

print 'From server: '
print response.decode() 
