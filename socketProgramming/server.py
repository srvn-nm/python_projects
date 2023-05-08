"""
@author: Sarvin Nami

"""
from socket import *
from threading import *

PORT = 7447

def main():
    address = gethostbyname(gethostname())
    HOST_info, mySocket = (address, PORT), socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(HOST_info)
    start(mySocket)
    
def start(server):
    print("Server is starting...")
    server.listen()
    while True:
        connection, address = server.accept()
        tread = Thread(target = clientHandler, args = (connection, address))
    
def clientHandler(connection, address):
    print(f"CLient from IP address {address} successfully connected! ^-^")
    connected = True
    
    
if __name__ == "__main__":
    main()