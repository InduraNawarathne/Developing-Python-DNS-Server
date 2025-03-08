# Basic DNS Server

## Project Description
This is a simple DNS server implemented in Python. It supports A and CNAME record queries, allowing clients to resolve domain names to IP addresses or alias names. The server listens for incoming DNS requests and responds based on predefined records.

## Features
- Supports A (IPv4) and CNAME (alias) records
- Listens for DNS queries on a specified port
- Parses and constructs DNS request and response packets
- Provides configurable domain mappings

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository or download the script:
   ```sh
   git clone <repository_url>
   cd basic-dns-server
   ```
2. Ensure you have Python installed:
   ```sh
   python --version
   ```
3. Run the DNS server:
   ```sh
   python dns_server.py
   ```

## How It Works
1. The server listens for incoming DNS requests.
2. It parses the DNS request packet to extract the queried domain.
3. If the domain exists in the server's records, it sends a response with the corresponding A or CNAME record.
4. If the domain is not found, it returns a DNS failure response.

## Example Usage
To test the DNS server, you can use the `nslookup` command:
```sh
nslookup example.com 127.0.0.1
```
Expected response:
```
Name:    example.com
Address: 192.168.1.100
```

## Known Issues
- Currently supports only A and CNAME records.
- Does not forward queries to an external DNS resolver.

## Author
Indura Nawarathne

