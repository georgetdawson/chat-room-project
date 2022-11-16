import logging

#Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\George\Documents\coding\chat-room-python\logfile.log",
                    level = logging.DEBUG,
                    filemode = 'w')
                    
logger = logging.getLogger()

#Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

# Importing socket and threading
logger.debug("importing socket and threading")

import socket
import threading

#Port and server variables
logger.debug ("port and server variables")

PORT = 6450
SERVER = socket.gethostbyname(socket.gethostname())
PRINT = (SERVER)

ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Incoming clients 
logger.debug ("incoming clients")

def incoming_clients(conn, addr):
    pass

def main():
    server.listen()
    print(f'Server has started listening for clients on (SERVER)...')
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target=incoming_clients,args=(conn,addr))
        thread.start()
        print(f'No of clients that are connected: {threading.activeCount() -1}')
        server.close()

#Server program has started message
logger.debug ("server program has started message.")

        print("Server Program has started..")
        main()
        




