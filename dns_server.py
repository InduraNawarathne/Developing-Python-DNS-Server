import socket
import threading

# Some sample DNS records (Both A and CNAME)
dns_records = {
    "example.com": {"A": "192.168.1.1"},
    "alias.com": {"CNAME": "example.com"},
    "myserver.com": {"A": "10.0.0.2"},
    "service.net": {"CNAME": "cloud.example.com"},
    "cicra.edu": {"A": "160.153.138.201"},
    "mail.service.net": {"CNAME": "service.net"},
}


class DNSServer:
    def __init__(self, host="0.0.0.0", port=53):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        print(f"DNS Server is running on {self.host}:{self.port}")

    def handle_request(self, data, addr):
        query = data.decode().strip()
        print(f"Received query: {query} from {addr}")

        response = "Hostname not found"
        if query in dns_records:
            if "A" in dns_records[query]:
                response = f"A {dns_records[query]['A']}"
            elif "CNAME" in dns_records[query]:
                response = f"CNAME {dns_records[query]['CNAME']}"

        self.server_socket.sendto(response.encode(), addr)

    def run(self):
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            threading.Thread(target=self.handle_request, args=(data, addr)).start()


if __name__ == "__main__":
    dns_server = DNSServer()
    dns_server.run()
