import argparse
import socket
import struct

# Function for scanning the IP range
def scan_ip_range(start_ip, end_ip, subnet_mask):
    active_machines = []

    start = struct.unpack("!I", socket.inet_aton(start_ip))[0]
    end = struct.unpack("!I", socket.inet_aton(end_ip))[0]

    num_addresses = 2 ** (32 - subnet_mask)

    network_address = start & end

    for i in range(num_addresses):
        current_ip = socket.inet_ntoa(struct.pack("!I", network_address + i))

        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((current_ip, 80))
            active_machines.append(current_ip)
            print("Machine {} is active".format(current_ip))
        except (socket.timeout, socket.error) as e:
            print("Error while connecting to {}: {}".format(current_ip, e))

    return active_machines

# Function for scanning open ports
def scan_open_ports(ip_address, start_port, end_port, protocol):
    open_ports = []

#type of protocol
    if protocol.lower() == 'tcp':
        socket_type = socket.SOCK_STREAM
    elif protocol.lower() == 'udp':
        socket_type = socket.SOCK_DGRAM
    else:
        print("Invalid protocol")
        return open_ports

#scan for available ports in the loop
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket_type)
            #timeout for quicker connection
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))

            if result != 0:
                print("Port {} is closed".format(port))
            else:
                open_ports.append(port)
                print("Port {} is open".format(port))

            sock.close()
        except socket.error:
            #if any error occurs, go to the next port
            pass

    return open_ports

# Function for saving into a .txt file
def save_report_to_txt(report, file_path):
    try:
        with open(file_path, 'w') as file:
            for line in report:
                file.write(str(line) + '\n')
        print("Report saved successfully to {}".format(file_path))
    except IOError:
        print("Could not write to file")

def main():
    parser = argparse.ArgumentParser(description='Network Scanner CLI Tool')

    parser.add_argument('--ipscan', action='store_true', help='Scan an IP range and find active machines')
    parser.add_argument('--portscan', action='store_true', help='Scan open TCP/UDP ports on a machine')
    parser.add_argument('--ip', nargs='+', help='IP address range')
    parser.add_argument('-m', type=int, help='Subnet mask')
    parser.add_argument('--tcp', nargs=2, type=int, help='TCP port range')
    parser.add_argument('--udp', nargs=2, type=int, help='UDP port range')

    args = parser.parse_args()

    if args.ipscan:
        if args.ip and args.m:
            scan_ip_range(args.ip[0], args.ip[1], args.m)
        else:
            print("Please provide IP address range and subnet mask")

    if args.portscan:
        if args.tcp:
            report = scan_open_ports('127.0.0.1', args.tcp[0], args.tcp[1], 'TCP')
            save_report_to_txt(report=report, file_path=r"C:\security\prj2.txt")
        elif args.udp:
            report = scan_open_ports('127.0.0.1', args.udp[0], args.udp[1], 'UDP')
            save_report_to_txt(report=report, file_path=r"C:\security\prj2.txt")
        else:
            print("Please specify TCP or UDP port range")

if __name__ == "__main__":
    main()
