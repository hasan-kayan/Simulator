# com_pac/core.py

from .tcp import TCPCommunication
from .udp import UDPCommunication
from .uart import UARTCommunication
from .ethernet import EthernetCommunication
from .config import DEFAULT_CONFIG

class CommunicationManager:
    """A centralized manager for handling multiple communication protocols."""

    def __init__(self, protocol: str, config: dict = None):
        """
        Initialize a communication instance based on the selected protocol.
        
        :param protocol: Communication protocol (TCP, UDP, UART, Ethernet)
        :param config: Custom configuration dictionary (optional)
        """
        self.protocol = protocol.upper()
        self.config = config if config else DEFAULT_CONFIG.get(self.protocol, {})

        self.comm_instance = self._initialize_protocol()

    def _initialize_protocol(self):
        """Initialize the correct communication class based on the protocol."""
        if self.protocol == "TCP":
            return TCPCommunication(self.config)
        elif self.protocol == "UDP":
            return UDPCommunication(self.config)
        elif self.protocol == "UART":
            return UARTCommunication(self.config)
        elif self.protocol == "ETHERNET":
            return EthernetCommunication(self.config)
        else:
            raise ValueError(f"Unsupported protocol: {self.protocol}")

    def open(self):
        """Open the communication channel."""
        self.comm_instance.open()

    def send(self, data):
        """Send data using the selected protocol."""
        self.comm_instance.send(data)

    def receive(self):
        """Receive data from the selected protocol."""
        return self.comm_instance.receive()

    def close(self):
        """Close the communication channel."""
        self.comm_instance.close()

    def __enter__(self):
        """Context manager support (with statement)."""
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the connection is closed when exiting the context."""
        self.close()
