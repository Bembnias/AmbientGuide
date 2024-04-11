import socket
import main
from connection import getIP
def udp_receive_send():
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    host = main.get_IP()  # Listen on all available addresses
    port = 2137
    udp_socket.bind((host, port))

    # Set the timeout for the socket to 3 seconds
    udp_socket.settimeout(3)

    while True:
        try:
            # Receive data
            data, address = udp_socket.recvfrom(1024)

            # Decode the received data
            message = data.decode('utf-8')

            # If the received message is "hello", send a response
            if message.strip() == "hello":
                response_message = "hello"
                udp_socket.sendto(response_message.encode('utf-8'), address)

        except socket.timeout:
            # If no packet is received within 3 seconds, call getIP
            ip_address = getIP()
            print(f"New IP address: {ip_address}")

        except KeyboardInterrupt:
            print("Stopping the server.")
            break

    # Close the socket
    udp_socket.close()
