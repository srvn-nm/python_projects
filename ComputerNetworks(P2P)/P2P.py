import json
from base64 import b64encode, b64decode
import socket

# Import standard Python modules for networking and multithreading support
import threading
import time
import random
import sys
import os
import asyncio
import logging
import struct

# Use Pillow (PIL fork) to handle image processing tasks
from PIL import Image as im

# Import Redis client module for interacting with Redis Cluster
try:
    import aioredis
    redis_client = aioredis.RedisCluster(
        startup_nodes=[
            {'host': 'localhost', 'port': 7000},
        ], db=0)  # Connect to local Redis instance on default port
    print("Connected to Redis")
except Exception as e:
    print('Failed connecting to Redis:', e)
    exit()

# Define constants used throughout the program
# IP/hostname and UDP port number of STUN server
STUN_SERVER = ('stun-server-ip', 1234)


def create_socket():

    """Create a raw socket suitable for sending and receiving UDP packets"""
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class PeerConnectionThread(threading.Thread):


    def __init__(self, conn, addr):


        super().__init__()
        self.conn = conn
        self.addr = addr


    def run(self):


        while True:
            try:
                msg = self.conn.recv(1024).decode()  # Receive message from connected peer
                if len(msg) > 0:
                    processMessage(msg)  # Process incoming message
            except OSError:
                break


class Server(object):


    def start(self):

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", PORT))
        sock.listen(1)
        print("Server listening...")
        while True:
                # Wait for a connection
            conn, addr = sock.accept()
            print("Client connected:", addr[0], ":", addr[1])

            # Start thread to manage client communication
            t = ClientHandler(conn, addr)
            t.start()


class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):


        super().__init__()
        self.conn = conn
        self.addr = addr


    def run(self):

            # Send welcome message to client
        self.sendMessage({"message": "Welcome! Please enter your username:"})

        # Continuously receive messages from client until disconnect
        while True:
            try:
                msg = self.conn.recv(1024).decode().strip('\n')
                if len(msg) == 0:
                    raise ConnectionError("Peer disconnected unexpectedly.")

                response = processInput(msg)
                if isinstance(response, str):
                    self.sendMessage({'message': response})

            except KeyboardInterrupt:
                quitProgram()
            except Exception as ex:
                logger.error(f"Exception occurred when communicating with {self.addr}: {ex}")
                continue


    def sendMessage(self, msgDict):


        encodedMsg = json.dumps(msgDict).encode() + b'\r\n'
        self.conn.sendall(encodedMsg)


    def processInput(inputStr):


        pass  # Replace this function with logic specific to your application


if __name__ == "__main__":
    server = Server()
    server.start()
