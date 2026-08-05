# daytime_server.py
# A simple server that sends the current date and time to any client that connects.

import socket
import datetime

HOST = 'localhost'  # Listen on the local machine only
PORT = 17000        # Any free port above 1023

def run_daytime_server():
    """Start the daytime server and listen for connections."""

    # 1. Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # 2. Allow the port to be reused immediately after the program restarts
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 3. Bind — attach the socket to the address and port
        server_socket.bind((HOST, PORT))

        # 4. Listen — start accepting connections (queue up to 5)
        server_socket.listen(5)
        print(f"Daytime server running on {HOST}:{PORT}")
        print("Press Ctrl+C to stop.\n")

        while True:
            # 5. Accept — pause here until a client connects
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection from {client_address}")

                # 6. Prepare the response — current date and time
                now = datetime.datetime.now()
                message = now.strftime("%A, %d %B %Y  %H:%M:%S\n")

                # 7. Send — data must be bytes, not a string
                client_socket.sendall(message.encode('utf-8'))
                print(f"Sent: {message.strip()}")
            # client_socket closes automatically here (with block ends)

if __name__ == '__main__':
    run_daytime_server()