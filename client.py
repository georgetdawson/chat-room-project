import logging

#Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\George\Documents\coding\chat-room-python\logfileclient.log",
                    level = logging.DEBUG,
                    filemode = 'w')
                    
logger = logging.getLogger()

#Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

import socket
import threading

#Defining header, server, port and disconnect message
logger.debug ("Defining header, server, port and disconnect message")

HEADER = 64
PORT = 6450
SERVER = SERVER = socket.gethostbyname(socket.gethostname())
PRINT = (SERVER)
DISCONNECT_MSG = '#DISCONNECT'

# configuring address and format
logger.debug ("configuring address and format")

ADDR = (SERVER,PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



#defining client
logger.debug ("defining client")

def client_main():
    connected = True
    send_msg("Connection has been established")
    while connected: 
        message = input("MSG: ")
        if message == 'disconnect':
            connected = False
            break
        send_msg(message)
    send(DISCONNECT_MSG)

client_main()

