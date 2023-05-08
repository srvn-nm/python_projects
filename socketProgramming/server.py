"""
@author: Sarvin Nami

"""
from socket import *
from threading import *
# defining port number, our tcp massage size and our encoding mode.
PORT, MASSAGE_SIZE, ENCODING = 7447, 64, "utf-8"

def main():
    # the ip address of my laptop as server 
    address = gethostbyname(gethostname())
    # defining host information and server socket
    HOST_info, serverSocket = (address, PORT), socket(AF_INET, SOCK_STREAM)
    # binding the server socket via host info
    serverSocket.bind(HOST_info)
    # starting the server ^-^
    start(serverSocket)
    
def start(server):
    print("Server is starting...")
    # server is waiting for clients
    server.listen()
    while True:
        # every moment server is ready to accept connections from clients
        connection, address = server.accept()
        # having a thread for each client
        thread = Thread(target = clientHandler, args = (connection, address))
        thread.start()
    
# thread function
def clientHandler(connection, address):
    print(f"CLient from IP address {address} successfully connected! ^-^")
    connected = True
    while connected:
        # figuring out the length of out massage and decoding it
        massageLen = int(connection.recv(MASSAGE_SIZE).decode(ENCODING))
        # reading the massage to reach the defined length and decoding it
        msg = connection.recv(massageLen).decode(ENCODING)
        print(f"New Massage:\n{msg}")
        # disconnect time T-T
        if msg == "DISCONNECT":
            connected = False
    # closing the connection
    connection.close()
    
if __name__ == "__main__":
    main()