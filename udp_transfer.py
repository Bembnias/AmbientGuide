import socket

def send_packet(message, number):
    ip_address = '192.168.0.0'
    port = 2137
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip_address, port)

    try:
        packet = f"{message}|{number}"
        sock.sendto(packet.encode(), server_address)
    finally:
        sock.close()

