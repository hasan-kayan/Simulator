import pytest
import socket
from unittest.mock import patch, MagicMock
from com_pac.udp import UDPCommunication
from com_pac.config import DEFAULT_CONFIG

@patch("socket.socket")
def test_udp(mock_socket):
    """Test UDP communication without a real server."""
    
    # Mock the socket instance
    mock_sock_instance = MagicMock()
    mock_socket.return_value = mock_sock_instance

    udp = UDPCommunication(DEFAULT_CONFIG["UDP"])
    udp.open()  # UDP is connectionless, so this won't do anything

    # Simulate sending data
    udp.send("Hello, UDP!")
    mock_sock_instance.sendto.assert_called_with(b"Hello, UDP!", (DEFAULT_CONFIG["UDP"]["host"], DEFAULT_CONFIG["UDP"]["port"]))

    # Simulate receiving data
    mock_sock_instance.recvfrom.return_value = (b"ACK", ("127.0.0.1", 5001))
    response = udp.receive()
    assert response == "ACK"

    udp.close()
    mock_sock_instance.close.assert_called()
