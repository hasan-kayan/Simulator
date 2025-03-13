from com_pac.tcp import TCPCommunication
from com_pac.config import DEFAULT_CONFIG

# Initialize TCP communication
tcp = TCPCommunication(DEFAULT_CONFIG["TCP"])

tcp.open()
tcp.send("Hello, world!")
response = tcp.receive()
print("Received:", response)
tcp.close()
