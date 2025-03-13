# com_pac/base.py

from abc import ABC, abstractmethod

class BaseCommunication(ABC):
    """Abstract base class for communication protocols."""
    """This class ensures that all protocols have a common structure."""
    
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def open(self):
        """Open the communication channel."""
        pass

    @abstractmethod
    def send(self, data):
        """Send data."""
        pass

    @abstractmethod
    def receive(self):
        """Receive data."""
        pass

    @abstractmethod
    def close(self):
        """Close the communication channel."""
        pass
