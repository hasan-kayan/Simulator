# **com_pac - A Configurable Communication Library**

`com_pac` is a Python library that provides configurable support for multiple communication protocols, including:
- **TCP/IP**
- **UDP**
- **UART (Serial)**
- **Ethernet (Raw Sockets)**

## **Project Structure**
Below is an overview of the project structure and the purpose of each file.

```
com_pac/
│── com_pac/               # Library source code
│   │── base.py            # Abstract base class for communication protocols
│   │── config.py          # Default configuration settings
│   │── core.py            # Main communication manager class
│   │── ethernet.py        # Ethernet (Raw Socket) communication class
│   │── __init__.py        # Package initialization
│   │── tcp.py             # TCP communication class
│   │── uart.py            # UART (Serial) communication class
│   │── udp.py             # UDP communication class
│── examples/              # Example scripts
│   └── example.py         # Sample usage of the communication library
│── LICENSE                # License information
│── pyproject.toml         # Build system configuration
│── requirements.txt       # Required dependencies
│── setup.cfg              # Configuration for setuptools
│── tests/                 # Unit test directory
│   ├── test_tcp.py        # Unit tests for TCP communication
│   ├── test_udp.py        # Unit tests for UDP communication
│   ├── test_uart.py       # Unit tests for UART communication
│   ├── test_ethernet.py   # Unit tests for Ethernet communication
```

---

## **Source Files**
### **1. `com_pac/base.py`**
Defines an **abstract base class** (`BaseCommunication`) for all communication protocols, enforcing a unified API.

- `open()` → Opens the communication channel.
- `send(data)` → Sends data over the communication channel.
- `receive()` → Receives data from the communication channel.
- `close()` → Closes the communication channel.

---

### **2. `com_pac/config.py`**
Contains default configurations for all communication protocols.

```python
DEFAULT_CONFIG = {
    "TCP": {"host": "127.0.0.1", "port": 5000},
    "UDP": {"host": "127.0.0.1", "port": 5001},
    "UART": {"port": "/dev/ttyUSB0", "baudrate": 9600, "timeout": 1},
    "Ethernet": {"interface": "eth0"}
}
```

---

### **3. `com_pac/core.py`**
Provides a **centralized communication manager** that dynamically selects the required communication protocol.

#### **Functions:**
- `__init__(protocol, config=None)` → Initializes the selected protocol.
- `_initialize_protocol()` → Dynamically loads the appropriate communication handler.
- `open()` → Opens the selected protocol.
- `send(data)` → Sends data through the selected protocol.
- `receive()` → Receives data from the selected protocol.
- `close()` → Closes the communication channel.

#### **Usage Example**
```python
from com_pac.core import CommunicationManager

with CommunicationManager("TCP") as tcp:
    tcp.send("Hello, TCP!")
    response = tcp.receive()
    print(response)
```

---

### **4. `com_pac/tcp.py`**
Implements **TCP communication** using Python's `socket` module.

#### **Functions:**
- `open()` → Establishes a TCP connection.
- `send(data)` → Sends data over TCP.
- `receive()` → Receives data from the TCP connection.
- `close()` → Closes the TCP connection.

---

### **5. `com_pac/udp.py`**
Implements **UDP communication**, which is connectionless.

#### **Functions:**
- `open()` → (Unused, since UDP does not establish connections).
- `send(data)` → Sends a UDP message.
- `receive()` → Receives a UDP message.
- `close()` → Closes the UDP socket.

---

### **6. `com_pac/uart.py`**
Implements **UART (Serial) communication** using `pyserial`.

#### **Functions:**
- `open()` → Opens the serial port.
- `send(data)` → Sends data over the serial port.
- `receive()` → Reads data from the serial port.
- `close()` → Closes the serial port.

---

### **7. `com_pac/ethernet.py`**
Handles **raw Ethernet communication** using `socket.AF_PACKET, socket.SOCK_RAW`.

#### **Functions:**
- `open()` → Binds to a network interface.
- `send(data)` → Sends raw Ethernet frames.
- `receive()` → Receives raw Ethernet frames.
- `close()` → Closes the Ethernet socket.

---

### **8. `com_pac/__init__.py`**
Initializes the package and provides easy access to all communication classes.

```python
from .tcp import TCPCommunication
from .udp import UDPCommunication
from .uart import UARTCommunication
from .ethernet import EthernetCommunication
from .config import DEFAULT_CONFIG

__all__ = ["TCPCommunication", "UDPCommunication", "UARTCommunication", "EthernetCommunication", "DEFAULT_CONFIG"]
```

---

## **Testing**
### **Run All Tests**
```sh
pytest tests/
```

### **Individual Test Files**
- `tests/test_tcp.py` → Tests TCP communication.
- `tests/test_udp.py` → Tests UDP communication.
- `tests/test_uart.py` → Tests UART communication.
- `tests/test_ethernet.py` → Tests Ethernet communication.

---

## **Installation & Deployment**
### **Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Install the Package Locally**
```sh
pip install -e .
```

### **Publish to PyPI**
1. Build the package:
   ```sh
   python -m build
   ```
2. Upload to PyPI:
   ```sh
   twine upload dist/*
   ```
3. Install it via:
   ```sh
   pip install com_pac
   ```

---

## **License**
This project is licensed under the **MIT License**.

---

## **Contributing**
Pull requests are welcome! Feel free to contribute by:
- Adding support for new protocols.
- Improving performance.
- Writing additional tests.

---

Now you have a **complete README** that explains **every file and function** in the project. 🚀
