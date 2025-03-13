# com_pac/__init__.py

"""
com_pac - A configurable communication library supporting:
- TCP/IP
- UDP
- UART (Serial)
- Ethernet

Usage:
    from com_pac import TCPCommunication, UDPCommunication, UARTCommunication, EthernetCommunication
"""

from .tcp import TCPCommunication
from .udp import UDPCommunication
from .uart import UARTCommunication
from .ethernet import EthernetCommunication
from .config import DEFAULT_CONFIG

__all__ = ["TCPCommunication", "UDPCommunication", "UARTCommunication", "EthernetCommunication", "DEFAULT_CONFIG"]
