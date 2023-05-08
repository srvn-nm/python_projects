"""
@author: Sarvin Nami

"""
from socket import *
from threading import *

PORT = 7447

def main():
    address = gethostbyname(gethostname())

    print(address)
    
    
if __name__ == "__main__":
    main()