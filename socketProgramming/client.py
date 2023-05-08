"""
@author: Sarvin Nami

"""
from socket import *

PORT, MASSAGE_SIZE, ENCODING = 7447, 64, "utf-8"

def main():
    clientSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
    address = gethostbyname(gethostname())
    SERVER_info = (address, PORT)
    clientSocket.connect(SERVER_info)
    sendMsg(clientSocket, "Hey Meow to everyone! ^-^")
    sendMsg(clientSocket, "DISCONNECT")
    
def sendMsg(client, msg):
    
    
if __name__ == "__main__":
    main()