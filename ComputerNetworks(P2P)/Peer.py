import json
import socket
import threading
from PIL import Image
import requests
import io


def is_port_busy(port):
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(1)
        tcp_socket.bind(("localhost", port))
        tcp_socket.close()
        # udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # udp_socket.settimeout(1)
        # udp_socket.bind(("localhost", port))
        # udp_socket.close()
        return False
    except socket.error:
        return True


def file_receiver(my_ip, target_ip, filename):
    empty_port = 1
    for ip in range(10001, 10011):
        if not is_port_busy(ip):
            empty_port = ip
    if empty_port == 1:
        print("You can't connect to ports right now! >-<")
        return
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_and_ip = (my_ip, 10000)
    tcp_socket.connect(port_and_ip)
    message = f"{target_ip}:{empty_port}:{filename}"
    tcp_socket.sendall(message.encode())
    data = tcp_socket.recv(1024)
    response = json.loads(data.decode())


    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((my_ip, empty_port))
    # Process received image/video data over UDP connection
    chunks = []
    while True:
        chunk, addr = udp_socket.recvfrom(1024)
        if not chunk:
            break
        chunks.append(chunk)

    # Combine the received chunks into a single byte string
    data = b''.join(chunks)
    try:
        received_image = Image.open(io.BytesIO(data))
        received_image.show()
        file = open(f'./file/{filename}', "wb")
        file.write(data)
    except:
        print("Error appeared while using the file!")

    # Close the sockets
    udp_socket.close()
    tcp_socket.close()


def file_sender(dest_ip, dest_port, dest_filename):
    HOST = dest_ip
    PORT = int(dest_port)
    BUFFER_SIZE = 1024

    try:
        with open('./files/' + dest_filename, 'rb') as f:
            data = f.read()
            is_string = True
    except FileNotFoundError:
        try:
            image = Image.open('./files/' + dest_filename)
            data = image.tobytes()
            is_string = False
        except FileNotFoundError:
            print("File couldn't be found! >-<")
            return


    if is_string:
        message = {"type": "string", "data": data}
    else:
        message = {"type": "image", "data": data}

    encoded_message = json.dumps(message).encode()


    if not is_string:
        # Send image data over UDP connection
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(0, len(data), BUFFER_SIZE):
            chunk = data[i:i + BUFFER_SIZE]
            udp_socket.sendto(chunk, (HOST, PORT))

        udp_socket.sendto(b'', (HOST, PORT))
        udp_socket.close()
    else:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((HOST, PORT))
        # Send the message over TCP connection
        tcp_socket.sendall(encoded_message)
        tcp_socket.close()


class Peer:
    def __init__(self):
        self.tcp_handshake_port = 10000
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.init_url = 'http://127.1.1.2:8080/init'
        self.get_usernames = 'http://127.1.1.2:8080/getAll'
        self.get_ip = 'http://127.1.1.2:8080/getIp?username='
        threading.Thread(target=self.listener, args=(self.ip_address, )).start()

    def listener(self, k):
        while True:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            local_address = (self.ip_address, self.tcp_handshake_port)
            # tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcp_socket.bind(local_address)
            tcp_socket.listen()
            client_sock, client_address = tcp_socket.accept()
            data = client_sock.recv(1024).decode('utf-8')
            data = data.split(':')
            dest_ip = data[0]
            dest_port = data[1]
            dest_filename = data[2]
            acceptance = False
            while True:
                inp = input(
                    f"A system with IP {client_address} wants to connect you and receive '{dest_filename}', do you want to accept?\n1. Yes\n2. No\nInput: ")
                if inp == '1':
                    acceptance = True
                    break
                elif inp == '2':
                    break
                else:
                    print('Invalid input!')
            if acceptance:
                tcp_socket.sendall(b"Done")
                threading.Thread(target=file_sender, args=(dest_ip, dest_port, dest_filename)).start()
            else:
                tcp_socket.sendall(b"None")
            tcp_socket.close()

    def init_action(self):
        print('init_action')
        username = input("Enter a username:")
        data = {
            "username": username,
            "ip": self.ip_address
        }
        try:
            response = requests.post(self.init_url, json=data).text
        except:
            response = "error"
        print('HTTP Server Response:', response)

    def get_usernames_action(self):
        print('get_usernames_action')
        try:
            response = requests.get(url=self.get_usernames).text
        except:
            response = "Error"
        print('HTTP Server Response:', response)

    def get_specific_ip_action(self):
        print("get_specific_ip_action")
        target_ip = input("Enter Target IP:")
        try:
            response = requests.get(self.get_ip + target_ip).text
        except:
            response = "Error"
        print('HTTP Server Response:', response)

    def request_for_connection_action(self):
        print('request_for_connection_action')
        target_ip = input('Enter your target IP: ')
        filename = input('Enter file route: ')
        threading.Thread(target=file_receiver, args=(self.ip_address, target_ip, filename)).start()

    def run(self):
        print("Hello ^-^\nYou can connect others in here for transferring data!\nWhenever you want to exit press enter!")
        choice = input('Choose one option below:\n1. Initialization\n2. Get near usernames\n3. Get specific IP\n4. Request for connection\nInput: ')
        while choice:
            if choice == '1':
                self.init_action()
            elif choice == '2':
                self.get_usernames_action()
            elif choice == '3':
                self.get_specific_ip_action()
            elif choice == '4':
                self.request_for_connection_action()
            else:
                print("Wrong choice! Please try again.")
            choice = input('Choose one option below:\n1. Initialization\n2. Get near usernames\n3. Get specific IP\n4. Request for connection\nInput: ')

if __name__ == "__main__":
    peer = Peer()
    peer.run()
