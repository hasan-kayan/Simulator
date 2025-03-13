# com_pac/uart.py

import serial
from .base import BaseCommunication

class UARTCommunication(BaseCommunication):
    """UART (Serial) communication handler."""

    def __init__(self, config):
        super().__init__(config)
        self.serial_port = serial.Serial()

    def open(self):
        """Open UART port."""
        self.serial_port.port = self.config["port"]
        self.serial_port.baudrate = self.config["baudrate"]
        self.serial_port.timeout = self.config.get("timeout", 1)
        self.serial_port.open()

    def send(self, data):
        """Send data over UART."""
        self.serial_port.write(data.encode())

    def receive(self):
        """Receive data over UART."""
        return self.serial_port.readline().decode().strip()

    def close(self):
        """Close UART port."""
        self.serial_port.close()
