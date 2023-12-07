import argparse
import socket
import struct


def scan_ip_range(start_ip, end_ip, subnet_mask):
    active_machines = []

    # تبدیل آدرس‌های IP به شکل عددی برای اسکن
    start = struct.unpack("!I", socket.inet_aton(start_ip))[0]
    end = struct.unpack("!I", socket.inet_aton(end_ip))[0]

    # Loop اسکن برای هر IP در محدوده مشخص شده
    for ip in range(start, end + 1):
        current_ip = socket.inet_ntoa(struct.pack("!I", ip))

        # تست کردن اتصال به IP جاری
        try:
            socket.setdefaulttimeout(1)  # تنظیم تایم‌اوت برای اتصال سریع‌تر
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((current_ip, 80))

            # اگر بتوان به پورت 80 متصل شد، IP فعال است
            active_machines.append(current_ip)
            print(f"Machine {current_ip} is active")
        except:
            pass  # اگر اتصال برقرار نشود، به IP بعدی برو

    return active_machines

def scan_open_ports(ip_address, start_port, end_port, protocol):
    open_ports = []

    # تعیین نوع پروتکل برای سوکت
    if protocol.lower() == 'tcp':
        socket_type = socket.SOCK_STREAM  # برای TCP
    elif protocol.lower() == 'udp':
        socket_type = socket.SOCK_DGRAM  # برای UDP
    else:
        print("Invalid protocol")
        return open_ports

    # Loop اسکن برای هر پورت در محدوده مشخص شده
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket_type)
            sock.settimeout(1)  # تنظیم تایم‌اوت برای اتصال سریع‌تر
            result = sock.connect_ex((ip_address, port))

            # اگر نتوان به پورت متصل شد، پورت بسته است
            if result != 0:
                print(f"Port {port} is closed")
            else:
                open_ports.append(port)
                print(f"Port {port} is open")

            sock.close()
        except socket.error:
            pass  # اگر خطایی رخ داد، به پورت بعدی برو

    return open_ports

def save_report_to_txt(report, file_path):
    try:
        with open(file_path, 'w') as file:
            for line in report:
                file.write(str(line) + '\n')
        print(f"Report saved successfully to {file_path}")
    except IOError:
        print("Could not write to file")

def main():
    parser = argparse.ArgumentParser(description='Network Scanner CLI Tool')

    parser.add_argument('--ipscan', action='store_true', help='Scan an IP range and find active machines')
    parser.add_argument('--portscan', action='store_true', help='Scan open TCP/UDP ports on a machine')
    parser.add_argument('--ip', nargs='+', help='IP address range')
    parser.add_argument('--m', type=int, help='Subnet mask')
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
            scan_open_ports('127.0.0.1', args.tcp[0], args.tcp[1], 'TCP')
            save_report_to_txt(report=args.tcp, file_path="C/prj2.txt")
        elif args.udp:
            scan_open_ports('127.0.0.1', args.udp[0], args.udp[1], 'UDP')
            save_report_to_txt(report=args.udp, file_path="C/prj2.txt")
        else:
            print("Please specify TCP or UDP port range")


if __name__ == "__main__":
    main()