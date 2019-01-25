from bluepy.btle import Peripheral
import time
from settings import Settings
from kalman import SingleStateKalmanFilter

# Initialise the Kalman Filter
A = 1  # No process innovation
C = 1  # Measurement
B = 0  # No control input
Q = 0.005  # Process covariance
R = .3  # Measurement covariance
x = 78  # Initial estimate
P = 1  # Initial covariance

kalman_filter = SingleStateKalmanFilter(A, B, C, x, P, Q, R)

# Empty lists for capturing filter estimates
kalman_filter_estimates = []

settings = Settings()

p = Peripheral(settings.mac_address, 'random')

try:
    object_temp_char = p.getCharacteristics(uuid=settings.object_temp_uuid)[0]
    ambient_temp_char = p.getCharacteristics(uuid=settings.ambient_temp_uuid)[0]

    while True:
        object_temp = float(str(object_temp_char.read())[2:-1])
        ambient_temp = ambient_temp_char.read()

        kalman_filter.step(0, object_temp)
        object_temp_filter = kalman_filter.current_state()
        print("%.2f" % object_temp)
        print("%.2f" % object_temp_filter)
        time.sleep(1)

finally:
    p.disconnect()
