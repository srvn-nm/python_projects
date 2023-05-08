"""
@author: Sarvin Nami

"""
from socket import *

# defining basic setting as server
PORT, MASSAGE_SIZE, ENCODING = 7447, 64, "utf-8"

def main():
    # defining client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # the ip address of my laptop as client
    address = gethostbyname(gethostname())
    # defining server information
    SERVER_info = (address, PORT)
    # connecting client socket to the server
    clientSocket.connect(SERVER_info)
    print("Client is up!")
    # sending massages and ending the connection
    sendMsg(clientSocket, "Hey Meow to everyone! ^-^")
    sendMsg(clientSocket, "DISCONNECT")
    
def sendMsg(client, msg):
    # encoding the massage
    massage = msg.encode(ENCODING)
    # calculating massage length, encoding it, turning it to bytes and sending it.
    msgLen = str(len(massage)).encode(ENCODING)
    msgLen += b' ' * (MASSAGE_SIZE - len(msgLen))
    client.send(msgLen)
    # sending the massage
    client.send(massage)
    
    
if __name__ == "__main__":
    main()