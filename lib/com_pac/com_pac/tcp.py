# com_pac/tcp.py

import socket
from .base import BaseCommunication

class TCPCommunication(BaseCommunication):
    """TCP/IP communication handler."""

    def __init__(self, config):
        super().__init__(config)
        self.socket = None

    def open(self):
        """Establish a TCP connection."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.config["host"], self.config["port"]))

    def send(self, data):
        """Send data over TCP."""
        self.socket.sendall(data.encode())

    def receive(self):
        """Receive data over TCP."""
        return self.socket.recv(1024).decode()

    def close(self):
        """Close the TCP connection."""
        self.socket.close()
