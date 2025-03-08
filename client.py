import socket


def dns_client():
    server_ip = input("Enter DNS server IP: ")
    server_port = int(input("Enter DNS server port: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        hostname = input("Enter hostname to resolve (or type 'exit' to quit): ")  # User can enter name to resolve
        if hostname.lower() == 'exit':
            break

        client_socket.sendto(hostname.encode(), (server_ip, server_port))
        response, _ = client_socket.recvfrom(1024)
        print(f"Response from DNS server: {response.decode()}")

    client_socket.close()


if __name__ == "__main__":
    dns_client()
