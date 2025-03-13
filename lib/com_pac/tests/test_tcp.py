import pytest
import socket
from unittest.mock import patch, MagicMock
from com_pac.tcp import TCPCommunication
from com_pac.config import DEFAULT_CONFIG

@patch("socket.socket")
def test_tcp(mock_socket):
    """Test TCP communication without a real server."""
    
    # Mock the socket instance
    mock_sock_instance = MagicMock()
    mock_socket.return_value = mock_sock_instance

    tcp = TCPCommunication(DEFAULT_CONFIG["TCP"])
    tcp.open()

    # Simulate sending data
    tcp.send("Hello, test!")
    mock_sock_instance.sendall.assert_called_with(b"Hello, test!")

    # Simulate receiving data
    mock_sock_instance.recv.return_value = b"OK"
    response = tcp.receive()
    assert response == "OK"

    tcp.close()
    mock_sock_instance.close.assert_called()
