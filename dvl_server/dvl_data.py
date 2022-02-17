from typing import List, Tuple

class DVL_DATA:

    def __init__(self) -> None:
        self.coordinates: List
        self.is_valid: bool
        self.count: int # Count of data packets
        self.struct_id: int # Structure id number
        self.version: str # Structure version number
        self.system_type: int # Should be 76 for Wayfinder
        self.system_subtype: int # 0 for Wayfinder
        self.fw_major_version: int
        self.fw_minor_version: int
        self.fw_patch_version: int
        self.fw_build_version: str
        self.year: int
        self.month: int
        self.day: int
        self.hour: int # range(24)
        self.minute: int # range(60)
        self.second: int # range(60)
        self.coordinate_system: int # (0-3)
        self.vel_x: float # Beam 1 in m/s
        self.vel_y: float # Beam 2 in m/s
        self.vel_z: float # Beam 3 in m/s
        self.vel_err: float # Beam 4 in m/s
        self.range_beam1: float # Beam 1 range to bottom in meters
        self.range_beam2: float # Beam 2 range to bottom in meters
        self.range_beam3: float # Beam 3 range to bottom in meters
        self.range_beam4: float # Beam 4 range to bottom in meters
        self.mean_range: float # Mean range to bottom in meters
        self.speed_of_sounds: float # Speed of sound used in m/s
        self.status
        self.bit_count
        self.bit_code
        self.voltage
        self.transit_voltage
        self.current
        self.serial_number


