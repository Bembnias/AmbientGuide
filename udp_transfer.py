import socket
import connection
import time
def send_packet(message, number):
    port = 2137
    ip = connection.get_IP()
    if ip is not None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (ip, port)

        try:
            packet = f"{message}|{number}"
            sock.sendto(packet.encode(), server_address)
            print(f"Sent {message}|{number}")
        finally:
            sock.close()

def send_packet_with_color(message, number, color):
    port = 2137
    ip = connection.get_IP()
    if ip is not None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (ip, port)

        try:
            packet = f"{message}{color}|{number}"
            sock.sendto(packet.encode(), server_address)
            print(f"Sent {message}{color}|{number}")
            time.sleep(2)
        finally:
            sock.close()