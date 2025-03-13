import pytest
import socket
from unittest.mock import patch, MagicMock
from com_pac.ethernet import EthernetCommunication
from com_pac.config import DEFAULT_CONFIG

@patch("socket.socket")
def test_ethernet(mock_socket):
    """Test Ethernet communication without a real network."""
    
    # Mock the socket instance
    mock_sock_instance = MagicMock()
    mock_socket.return_value = mock_sock_instance

    ethernet = EthernetCommunication(DEFAULT_CONFIG["Ethernet"])
    ethernet.open()

    # Simulate sending data
    ethernet.send(b"Hello, Ethernet!")
    mock_sock_instance.send.assert_called_with(b"Hello, Ethernet!")

    # Simulate receiving data
    mock_sock_instance.recv.return_value = b"ACK"
    response = ethernet.receive()
    assert response == b"ACK"

    ethernet.close()
    mock_sock_instance.close.assert_called()
