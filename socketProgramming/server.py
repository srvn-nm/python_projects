"""
@author: Sarvin Nami

"""
from socket import *
from threading import *

PORT = 7447

def main():
    address = gethostbyname(gethostname())

    HOST_info = (address, PORT)
    
    mySocket = socket(socket.AF_INET, socket.SOCK_STREAM)
    
    mySocket.bind(HOST_info)
    
def start():
    print("Server is starting...")
    
    
    
if __name__ == "__main__":
    main()