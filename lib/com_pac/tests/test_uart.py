import pytest
from unittest.mock import patch, MagicMock
from com_pac.uart import UARTCommunication
from com_pac.config import DEFAULT_CONFIG

@patch("serial.Serial")
def test_uart(mock_serial):
    """Test UART communication without a real device."""
    
    # Mock the serial instance
    mock_serial_instance = MagicMock()
    mock_serial.return_value = mock_serial_instance

    uart = UARTCommunication(DEFAULT_CONFIG["UART"])
    uart.open()

    # Simulate sending data
    uart.send("Hello, UART!")
    mock_serial_instance.write.assert_called_with(b"Hello, UART!")

    # Simulate receiving data
    mock_serial_instance.readline.return_value = b"Response\n"
    response = uart.receive()
    assert response == "Response"

    uart.close()
    mock_serial_instance.close.assert_called()
