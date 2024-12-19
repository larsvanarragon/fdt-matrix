import socket

# logging
import logging
logger = logging.getLogger(__name__)

from label_adapter import LabelAdapter
from callback_handler import CallbackHandler

DEFAULT_TORXAKIS_ADDRESS = "localhost"
DEFAULT_TORXAKIS_PORT = 7890
DEFAULT_TORXAKIS_DELIMITER = "\n"

class TorxakisConnection(CallbackHandler):

    def __init__(self, label_adapter: LabelAdapter, torxakis_address=DEFAULT_TORXAKIS_ADDRESS, torxakis_port=DEFAULT_TORXAKIS_PORT):
        self.torxakis_address = torxakis_address
        self.torxakis_port = torxakis_port
        self.label_adapter = label_adapter
        label_adapter.register_callback_handler(self)

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.torxakis_address, self.torxakis_port))
            sock.listen()
            connection, address = sock.accept()
            
            with connection, connection.makefile('r', encoding='utf8') as sock_file:
                logger.info(f"connected to TorXakis on {address}")
                self.connection = connection

                while True:
                    line = sock_file.readline()
                    if not line:
                        continue
                    logger.debug(f"received line '{line}' from torxakis")
                    self.label_adapter.handle_label(line.rstrip())

    def callback(self, label: str):
        logger.debug(f"sending {label} to torxakis")
        to_send = f"{label}{DEFAULT_TORXAKIS_DELIMITER}"
        self.connection.send(to_send.encode("utf-8"))

    # def connect_to_torxakis():
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #         sock.bind((TORXAKIS_ADDRESS, TORXAKIS_PORT))
    #         sock.listen()

    #         connection, address = sock.accept()
    #         with connection:
    #             logger.info(f"connected to TorXakis on {address}")
    #             while True:
    #                 data = connection.recv(1024)
    #                 if not data:
    #                     continue  
    #                 logger.info(f"received data {data}")
    #                 connection.send(b"ASentMessage(\"someMessage\")\n")
    #                 connection.send(b"Ok\n")

