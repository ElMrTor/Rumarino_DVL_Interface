"""Example usage for DVL driver (software trigger)
"""
from time import sleep
from dvl.dvl import Dvl
from dvl.system import OutputData

def get_types(objects):
    data_f = open('dvl_data', 'a')
    data_f.write('\n')
    
    for key, val in objects.items():
        print(f'{key} ------- {val} as --> {type(val)}')
        data_f.write(f'{key} ------- {val} as --> {type(val)}\n')
    data_f.write('\n')
    data_f.close()

def update_data(output_data: OutputData, obj):
    """Prints data time to screen
    """
    del obj
    if output_data is not None:
        time = output_data.get_date_time()
        txt = time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        info = vars(output_data)
        print("Got data {0}".format(txt))
        print(f'ObjectData:\n{info}\n')
        print(f'ObjectDataType:')
        get_types(info)

if __name__ == "__main__":
    PORT = input("Please enter your port number (e.g. '1' for COM1) =  ")
    PORT = "/dev/ttyUSB" + PORT

    # Initialize Dvl class
    with Dvl() as DVL:
        
        # Connect to serial port
        if DVL.connect(PORT):
            # Get user system setup
            if not DVL.get_setup():
                print("Failed to get system setup")
            else:
                # Print setup 
                print (DVL.system_setup)

                # Modify system setup structure to set software trigger
                SETUP = DVL.system_setup
                SETUP.software_trigger = 1

                # Set user system setup
                if not DVL.set_setup(SETUP):
                    print("Failed to set system setup")
                else:

                    # Collect data - make sure working folder exists
                    # if not DVL.start_logging("c:/temp", "DVL"):
                    if not DVL.start_logging("/home/hector/Documents/Rumarino/DVL_Workspace/Wayfinder/examples/data_example_logging", "DVL"):
                        print("Failed to start logging")
                    else:
                        print("Data logged to {0}".format(DVL.get_log_file_name()))

                    # Register callback function
                    DVL.register_ondata_callback(update_data)

                    # Exit command mode
                    if not DVL.exit_command_mode():
                        print("Failed to exit command mode")

                    print("Software trigger every 2 seconds - press Ctrl+C to stop")
                    RUN = True
                    while RUN:
                        try:
                            # Ping every 2 seconds
                            sleep(2)
                            if not DVL.send_software_trigger():
                                print("Failed to send software trigger")
                        except KeyboardInterrupt:
                            RUN = False

        else:
            print("Failed to open {0} - make sure it is not used by any other program".format(PORT))

