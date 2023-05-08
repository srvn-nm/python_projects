"""
@author: Sarvin Nami

"""
from socket import *

PORT, MASSAGE_SIZE, ENCODING = 7447, 64, "utf-8"

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    address = gethostbyname(gethostname())
    SERVER_info = (address, PORT)
    clientSocket.connect(SERVER_info)
    print("Client is up!")
    sendMsg(clientSocket, "Hey Meow to everyone! ^-^")
    sendMsg(clientSocket, "DISCONNECT")
    
def sendMsg(client, msg):
    massage = msg.encode(ENCODING)
    msgLen = str(len(massage)).encode(ENCODING)
    msgLen += b' ' * (MASSAGE_SIZE - len(msgLen))
    client.send(msgLen)
    client.send(massage)
    
    
if __name__ == "__main__":
    main()