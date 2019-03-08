from socket import *
import sys
import datetime

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket = socket(AF_INET, SOCK_DGRAM)

# set socket timeout to 1 second
clientSocket.settimeout(1)

for i in range(1,11):
	
	try: 

		s = str(i)
		sendtime = datetime.datetime.now()
		t = str(sendtime)
		message = 'ping ' + s + ' ' + t
		clientSocket.sendto(message.encode(), (serverName, serverPort))
		replyMessage, serverAddress = clientSocket.recvfrom(2048)

		# set up for calculating RTT
		backtime = datetime.datetime.now()
		m1_s = sendtime.strftime('%M')
		m1 = int(m1_s)
		m2_s = backtime.strftime('%M')
		m2 = int(m2_s)
		s1_s = sendtime.strftime('%S.%f')
		s1 = float(s1_s)
		s2_s = backtime.strftime('%S.%f')
		s2 = float(s2_s)

		print(replyMessage.decode())

		if m2 == m1:
			RTT = s2 - s1
			print 'RTT = ' + str(RTT) + ' seconds'
		elif m2 > m1:
			RTT = s2 + 60 - s1
			print 'RTT = ' + str(RTT) + ' seconds'

	except timeout:
		print 'Request timed out'
		continue 

clientSocket.close()
