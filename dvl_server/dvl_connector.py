from random import Random
from dvl_data import DVL_DATA
from datetime import datetime
from math import nan, isnan


def _check_for_nan(data: DVL_DATA):
    '''NaN values give errors in json format, therefore are converted to -1.0'''
    for attr, val in vars(data).items():
        if isinstance(val, float) and isnan(val):
            setattr(data, attr, -1.0)
    return vars(data)


class DVLDevice:       

    def get_data(self):
        return {'DVL_Data' : _check_for_nan(self.get_dvl_data())}

    def get_dvl_data(self):
        raise NotImplementedError


class WayfinderDVL(DVLDevice):
    pass

class DVLDummyDevice(DVLDevice):

    def __init__(self) -> None:
        self.rand = Random()        
        self.dvl_data = DVL_DATA()
        

    def get_dummy_data(self):
        self.prepare_random_data()
        return self.dvl_data

    def get_dummy_data_as_json(self):
        self.prepare_random_data()
        return {'DVL_Data' : vars(self.dvl_data)} 

    def get_dvl_data(self):
        self.prepare_random_data()
        return self.dvl_data
    
    def prepare_random_data(self):
        self.dvl_data.is_valid = self.rand.choice((True, False))
        self.dvl_data.count = self.rand.randint(0, 255) # From the collected example data it's always 0
        self.dvl_data.struct_id = self.rand.randint(0, 255) # From the collected example data it's always 170
        self.dvl_data.version = 17 # From collected example data
        self.dvl_data.system_type = 76 # From wayfinder documentation
        self.dvl_data.system_subtype = 0 # From wayfinder documentation
        self.dvl_data.fw_major_version = 1
        self.dvl_data.fw_minor_version = 0
        self.dvl_data.fw_patch_version = 0
        self.dvl_data.fw_build_version = 46
        self.dvl_data.year = datetime.now().year
        self.dvl_data.month = datetime.now().month
        self.dvl_data.day = datetime.now().day
        self.dvl_data.hour = datetime.now().hour
        self.dvl_data.minute = datetime.now().minute
        self.dvl_data.second = datetime.now().second
        self.dvl_data.coordinate_system = self.rand.randint(0, 3) # From Wayfinder documentation
        self.dvl_data.vel_x = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.vel_y = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.vel_z = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.range_beam1 = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.range_beam2 = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.range_beam3 = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.range_beam4 = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.mean_range = self.rand.choice((self.rand.uniform(0, 10000), nan))
        self.dvl_data.speed_of_sound = self.rand.uniform(0, 10000)
        self.dvl_data.status = 255
        self.dvl_data.bit_code = self.rand.randint(0, 255)
        self.dvl_data.bit_count = self.rand.randint(0, 255)
        self.dvl_data.voltage = self.rand.uniform(0, 500)
        self.dvl_data.transmit_voltage = self.rand.uniform(0, 500)
        self.dvl_data.current = self.rand.uniform(0, 500)
        self.dvl_data.serial_number = '001010' # From collected example data

        

        

