import json
import socket
import threading
from PIL import Image
import requests
import io


class Peer:
    def __init__(self):
        self.tcp_handshake_port = 10001
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.init_url = 'http://127.1.1.2:8080/init'
        self.get_usernames = 'http://127.1.1.2:8080/getAll'
        self.get_ip = 'http://127.1.1.2:8080/getIp?username='
        threading.Thread(target=self.listener).start()

    def is_port_busy(port):
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(1)
            tcp_socket.bind(("localhost", port))
            tcp_socket.close()
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(1)
            udp_socket.bind(("localhost", port))
            udp_socket.close()
            return False
        except socket.error:
            return True

    def file_sender(dest_ip, dest_port, dest_filename):
        HOST = dest_ip
        PORT = int(dest_port)
        BUFFER_SIZE = 1024

        try:
            with open('./files/' + dest_filename, 'r') as f:
                data = f.read()
                is_string = True
        except FileNotFoundError:
            try:
                image = Image.open('./files/' + dest_filename)
                data = image.tobytes()
                is_string = False
            except FileNotFoundError:
                print("File could'nt be found! >-<")
                return

        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((HOST, PORT))

        if is_string:
            message = {"type": "string", "data": data}
        else:
            message = {"type": "image", "data": data}

        encoded_message = json.dumps(message).encode()

        # Send the message over TCP connection
        tcp_socket.sendall(encoded_message)

        if not is_string:
            # Send image data over UDP connection
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for i in range(0, len(data), BUFFER_SIZE):
                chunk = data[i:i + BUFFER_SIZE]
                udp_socket.sendto(chunk, (HOST, PORT))

            udp_socket.sendto(b'', (HOST, PORT))
            udp_socket.close()

        tcp_socket.close()

    def file_receiver(self, my_ip, target_ip, filename):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = (target_ip, 10000)
        sock.connect(port_and_ip)
        empty_port = 1
        for i in range(10001, 10011):
            if not self.is_port_busy(empty_port):
                empty_port = i
        if empty_port == 1:
            print("You don't have any free legal port!!")
            return
        message = f"{my_ip}:{empty_port}:{filename}"
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((my_ip, empty_port))
        sock.sendall(message.encode())

        data = sock.recv(1024)
        response = json.loads(data.decode())

        if response["type"] == "string":
            # Process received text data over TCP connection
            received_text = response["data"]
            print("Received text:", received_text)
        elif response["type"] == "image":
            # Process received image/video data over UDP connection
            chunks = []
            while True:
                chunk, addr = udp_socket.recvfrom(1024)
                if not chunk:
                    break
                chunks.append(chunk)

            # Combine the received chunks into a single byte string
            data = b''.join(chunks)
            received_image = Image.open(io.BytesIO(data))
            received_image.show()

        # Close the sockets
        udp_socket.close()
        sock.close()

    def listener(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            local_address = (self.ip_address, self.tcp_handshake_port)
            sock.bind(local_address)
            sock.listen()
            client_sock, client_address = sock.accept()
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
                sock.sendall(b"Done")
                threading.Thread(target=self.file_sender, args=(dest_ip, dest_port, dest_filename)).start()
            else:
                sock.sendall(b"None")
            sock.close()

    def init_action(self):
        username = input("Enter a username:")
        data = {
            "username": username,
            "ip": self.ip_address
        }
        response = requests.post(self.init_url, json=data)
        print('HTTP Server Response:', response.text)

    def get_usernames_action(self):
        response = requests.get(self.get_usernames)
        print('HTTP Server Response:', response.text)

    def get_specific_ip_action(self):
        target_ip = input("Enter Target IP:")
        response = requests.get(self.get_ip + target_ip)
        print('HTTP Server Response:', response.text)

    def request_for_connection_action(self):
        target_ip = input('Enter your target IP:')
        filename = input('Enter filename:')
        threading.Thread(target=self.file_receiver, args=(self.ip_address, target_ip, filename)).start()

    def run(self):
        print("Welcome to this p2p app")
        while True:
            inp = input('Choose your action:\n1. Init\n2. Get usernames\n3. Get specific IP\n4. Request for connection\nInput: ')
            if inp == '1':
                self.init_action()
            elif inp == '2':
                self.get_usernames_action()
            elif inp == '3':
                self.get_specific_ip_action()
            elif inp == '4':
                self.request_for_connection_action()
            else:
                print("Wrong command!!")


if __name__ == "__main__":
    peer = Peer()
    peer.run()
