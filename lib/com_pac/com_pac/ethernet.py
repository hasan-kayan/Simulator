# com_pac/ethernet.py

import socket
from .base import BaseCommunication

class EthernetCommunication(BaseCommunication):
    """Ethernet (low-level) communication handler."""

    def __init__(self, config):
        super().__init__(config)
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    def open(self):
        """Bind to a network interface."""
        self.socket.bind((self.config["interface"], 0))

    def send(self, data):
        """Send raw Ethernet frames."""
        self.socket.send(data)

    def receive(self):
        """Receive raw Ethernet frames."""
        return self.socket.recv(65535)

    def close(self):
        """Close Ethernet socket."""
        self.socket.close()
