from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.uvic.ca'
portnumber = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,portnumber))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO tlin\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
command = 'mail from: tlin@uvic.ca\r\n'
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send RCPT TO command and print server response. 
command = 'rcpt to: <tylerlin113093@gmail.com>\r\n'
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send DATA command and print server response. 
command = 'data\r\n'
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send QUIT command and get server response.
command = 'quit\r\n'
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
