# com_pac/udp.py

import socket
from .base import BaseCommunication

class UDPCommunication(BaseCommunication):
    """UDP communication handler."""

    def __init__(self, config):
        super().__init__(config)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def open(self):
        """UDP is connectionless, so no need to open a connection."""
        pass

    def send(self, data):
        """Send data over UDP."""
        self.socket.sendto(data.encode(), (self.config["host"], self.config["port"]))

    def receive(self):
        """Receive data over UDP."""
        data, _ = self.socket.recvfrom(1024)
        return data.decode()

    def close(self):
        """Close the UDP socket."""
        self.socket.close()
