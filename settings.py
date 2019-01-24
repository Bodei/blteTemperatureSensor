from bluepy.btle import UUID

class Settings():

    def __init__(self):

        # Characteristics UUIDs
        self.object_temp_uuid  = UUID('c3940228-ed02-4452-962e-aed4c68ec80b')
        self.ambient_temp_uuid = UUID('c22535cd-c849-45f5-bdef-f47729ea5147')

        # Peripheral mac address
        self.mac_address       = 'D5:76:AF:0E:EB:DC'

