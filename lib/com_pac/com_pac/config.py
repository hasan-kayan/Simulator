# com_pac/config.py

DEFAULT_CONFIG = {
    "TCP": {"host": "127.0.0.1", "port": 5000},
    "UDP": {"host": "127.0.0.1", "port": 5001},
    "UART": {"port": "/dev/ttyUSB0", "baudrate": 9600, "timeout": 1},
    "Ethernet": {"interface": "eth0"}
}
