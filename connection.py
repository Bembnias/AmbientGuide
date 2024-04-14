import socket
import time

global ip_address
ip_address = None  # Initialize ip_address variable


def get_IP():
    return ip_address


def set_IP(ip):
    global ip_address
    ip_address = ip


def getIP():
    global ip_address
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = '0.0.0.0'
    port = 2137
    udp_socket.bind((host, port))

    print(f"Listening on port {port}...")

    try:
        while True:
            data, address = udp_socket.recvfrom(1024)

            message = data.decode('utf-8')

            if message.strip() == "2137":
                print(f"Received '2137' message from {address[0]}")

                response_message = "Response to '2137' message"
                udp_socket.sendto(response_message.encode('utf-8'), address)
                print("Sent response.")
                set_IP(address[0])
                udp_socket.close()
                check_device_availability()
                return

    except KeyboardInterrupt:
        print("Interrupted.")
        udp_socket.close()


def check_device_availability():
    global ip_address
    global start_time
    if ip_address is not None:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        host = '0.0.0.0'
        port = 2137
        udp_socket.bind((host, port))

        print(f"Listening on port {port}...")

        start_time = time.time()

        try:
            while True:
                data, address = udp_socket.recvfrom(1024)

                message = data.decode('utf-8')

                if message.strip() == "AmbientGuide_Check_Connect":
                    print(f"Received {message.strip()} message from {address[0]}")

                    response_message = "AmbientGuide_Check_Connect"
                    udp_socket.sendto(response_message.encode('utf-8'), address)
                    print("Sent response.")
                    set_IP(address[0])
                    start_time = time.time()
                    udp_socket.close()
                    check_device_availability()
                    return

                # Zresetuj czas, jeśli otrzymasz pakiet


                # Sprawdź, czy minęło więcej niż 6 sekund od ostatniego pakietu
                if time.time() - start_time > 3:
                    print("Connection timeout.")
                    ip_address = None
                    udp_socket.close()
                    getIP()

        except KeyboardInterrupt:
            print("Interrupted.")
            udp_socket.close()
    else:
        getIP()