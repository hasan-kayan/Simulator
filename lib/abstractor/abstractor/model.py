from typing import List, Optional, Dict

class Pin:
    def __init__(self, number: int, name: str, function: str, pin_type: str, voltage_level: Optional[float] = None):
        self.number = number
        self.name = name
        self.function = function
        self.pin_type = pin_type  # e.g., 'input', 'output', 'power', 'ground', 'bidirectional'
        self.voltage_level = voltage_level
class Type:
    def __init__(self, type_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.type_name = type_name
        self.description = description
        self.pins = pins if pins is not None else []
class Data: 
    def __init__(self, data_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.data_name = data_name
        self.description = description
        self.pins = pins if pins is not None else []
    def get_data_name(self):
        return self.data_name
class Signal:
    def __init__(self, signal_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.signal_name = signal_name
        self.description = description
        self.pins = pins if pins is not None else []
class Power:
    def __init__(self, power_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.power_name = power_name
        self.description = description
        self.pins = pins if pins is not None else []
class Ground:
    def __init__(self, ground_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.ground_name = ground_name
        self.description = description
        self.pins = pins if pins is not None else []
class Bidirectional:
    def __init__(self, bidirectional_name: str, description: Optional[str] = None, pins: Optional[List[Pin]] = None):
        self.bidirectional_name = bidirectional_name
        self.description = description
        self.pins = pins if pins is not None else []

class CommunicationProtocol:
    def __init__(self, protocol_name: str, data_rate: Optional[str] = None, voltage_levels: Optional[str] = None, addressing: Optional[str] = None):
        self.protocol_name = protocol_name  # e.g., 'I2C', 'SPI', 'UART', 'SMBus'
        self.data_rate = data_rate
        self.voltage_levels = voltage_levels
        self.addressing = addressing

class ElectricalCharacteristics:
    def __init__(self, operating_voltage: Optional[float] = None, power_consumption: Optional[float] = None, input_voltage_levels: Optional[Dict[str, float]] = None, output_voltage_levels: Optional[Dict[str, float]] = None):
        self.operating_voltage = operating_voltage
        self.power_consumption = power_consumption
        self.input_voltage_levels = input_voltage_levels  # e.g., {'high': 2.0, 'low': 0.8}
        self.output_voltage_levels = output_voltage_levels  # e.g., {'high': 2.9, 'low': 0.4}

class DataFormat:
    def __init__(self, data_width: Optional[str] = None, data_encoding: Optional[str] = None, supported_data_rates: Optional[List[str]] = None):
        self.data_width = data_width  # e.g., '8-bit', '16-bit'
        self.data_encoding = data_encoding  # e.g., 'binary', 'ASCII'
        self.supported_data_rates = supported_data_rates


class ElectronicComponent:
    def __init__(self, name: str, manufacturer: Optional[str] = None, description: Optional[str] = None, types: Optional[List[Type]] = None, datas: Optional[List[Data]] = None, signals: Optional[List[Signal]] = None, powers: Optional[List[Power]] = None, grounds: Optional[List[Ground]] = None, bidirectionals: Optional[List[Bidirectional]] = None, compliance: Optional[List[str]] = None):
        self.name = name
        self.manufacturer = manufacturer
        self.description = description
        self.types = types if types is not None else []
        self.datas = datas if datas is not None else []
        self.signals = signals if signals is not None else []
        self.powers = powers if powers is not None else []
        self.grounds = grounds if grounds is not None else []
        self.bidirectionals = bidirectionals if bidirectionals is not None else []
        self.compliance = compliance  # e.g., ['RoHS', 'IEC 61360']
    def add_type(self, type: Type):
        self.types.append(type)
    def add_data(self, data: Data):
        self.datas.append(data)
    def add_signal(self, signal: Signal):
        self.signals.append(signal)
    def add_power(self, power: Power):
        self.powers.append(power)
    def add_ground(self, ground: Ground):
        self.grounds.append(ground)
    def add_bidirectional(self, bidirectional: Bidirectional):
        self.bidirectionals.append(bidirectional)
