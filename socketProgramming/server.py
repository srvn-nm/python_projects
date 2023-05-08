"""
@author: Sarvin Nami

"""
from socket import *
from threading import *

PORT, MASSAGE_SIZE, ENCODING = 7447, 64, "utf-8"

def main():
    address = gethostbyname(gethostname())
    HOST_info, serverSocket = (address, PORT), socket(socket.AF_INET, socket.SOCK_STREAM)
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
    while connected:
        massageLen = int(connection.recv(MASSAGE_SIZE).decode(ENCODING))
        msg = connection.recv(massageLen).decode(ENCODING)
        print(f"New Massage:\n{msg}")
        if msg == "DISCONNECT":
            connected = False
    connection.close()
    
if __name__ == "__main__":
    main()