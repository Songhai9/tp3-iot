import socket

PORT_RECV = 8888
BUFSIZE = 64

# Create a socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

try:
    # Bind the socket to the address and port
    sock.bind(("::", PORT_RECV))
    print(f"UDP server is running on port {PORT_RECV}")

    while True:
        # Receive a message from the client
        data, client_addr = sock.recvfrom(BUFSIZE)
        client_ip, client_port, _, _ = client_addr

        # Decode the received message using ISO-8859-1 and handle any decoding errors
        try:
            message = data.decode('iso-8859-1')
        except UnicodeDecodeError:
            message = f"<Non-ISO-8859-1 data: {data}>"

        # Print the received message
        print(f"Received message from {client_ip}: {message}")

except KeyboardInterrupt:
    print("\nServer shutting down.")

finally:
    sock.close()
