import socket
from main import get_IP

def send_packet(message, number):
    port = 2137
    ip = get_IP()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, port)

    try:
        packet = f"{message}|{number}"
        sock.sendto(packet.encode(), server_address)
    finally:
        sock.close()

