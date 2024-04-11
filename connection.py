import socket
import sys

def getIP():
    # Tworzenie gniazda UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Powiązanie gniazda z adresem i portem
    host = '0.0.0.0'  # Nasłuchujemy na wszystkich adresach IP
    port = 2137
    udp_socket.bind((host, port))

    print(f"Nasłuchiwanie na porcie {port}...")

    try:
        while True:
            # Odbieranie danych
            data, address = udp_socket.recvfrom(1024)

            # Dekodowanie odebranych danych
            message = data.decode('utf-8')

            # Jeśli otrzymana wiadomość to "2137", wypisz adres IP nadawcy
            if message.strip() == "2137":
                print(f"Otrzymano wiadomość '2137' od {address[0]}")

                # Wysyłanie odpowiedzi na znany adres IP
                response_message = "Odpowiedź na wiadomość '2137'"
                udp_socket.sendto(response_message.encode('utf-8'), address)
                print("Wysłano odpowiedź.")

                return address[0]
    except KeyboardInterrupt:
        print("Przerwano nasłuchiwanie.")
        sys.exit(0)
        print("Przerwano nasłuchiwanie.")
        return '0.0.0.0'
    finally:
        # Zamykanie gniazda
        udp_socket.close()
        return '0.0.0.0'

