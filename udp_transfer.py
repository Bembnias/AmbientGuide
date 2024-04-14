import socket
import connection

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