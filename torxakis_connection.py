import socket

# logging
import logging
logger = logging.getLogger(__name__)

TORXAKIS_ADDRESS = "localhost"
TORXAKIS_PORT = 7890

def connect_to_torxakis():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((TORXAKIS_ADDRESS, TORXAKIS_PORT))
        sock.listen()

        connection, address = sock.accept()
        with connection:
            logger.info(f"connected to TorXakis on {address}")
            while True:
                data = connection.recv(1024)
                if not data:
                    continue  
                logger.info(f"received data {data}")
                connection.send(b"ASentMessage(\"someMessage\")\n")
                connection.send(b"Ok\n")

