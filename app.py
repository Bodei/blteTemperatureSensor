import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import datetime as dt

from bluepy.btle import Peripheral
from settings import Settings
from kalman import SingleStateKalmanFilter
from matplotlib.ticker import MultipleLocator, ScalarFormatter

# Initialise the Kalman Filter
A = 1  # No process innovation
C = 1  # Measurement
B = 0  # No control input
Q = 0.005  # Process covariance
R = 1  # Measurement covariance
x = 78  # Initial estimate
P = 1  # Initial covariance

kalman_filter = SingleStateKalmanFilter(A, B, C, x, P, Q, R)

# Empty lists for capturing filter estimates
kalman_filter_estimates = []



settings = Settings()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs1 = []
ys1 = []
ys2 = []



p = Peripheral(settings.mac_address, 'random')

try:
    object_temp_char = p.getCharacteristics(uuid=settings.object_temp_uuid)[0]
    ambient_temp_char = p.getCharacteristics(uuid=settings.ambient_temp_uuid)[0]

    def animate(i, xs1, ys1, ys2, kalman_filter_estimates):
        object_temp = object_temp_char.read()
        ambient_temp = ambient_temp_char.read()

        kalman_filter.step(0, float(str(object_temp)[2:-1]))
        print(float(str(object_temp)[2:-1]))
        print(kalman_filter.current_state())

        # Add x and y to lists
        xs1.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys1.append(kalman_filter.current_state())
        ys2.append(float(str(object_temp)[2:-1]))

        # Limit x and y lists to 20 items
        xs1 = xs1[-60:]
        ys1 = ys1[-60:]
        ys2 = ys2[-60:]

        # Draw x and y lists
        ax1.clear()
        ax1.plot(xs1, ys1, xs1, ys2)

        majorLocator = MultipleLocator(10)
        majorFormatter = ScalarFormatter()
        minorLocator = MultipleLocator(5)

        ax1.xaxis.set_major_locator(majorLocator)
        ax1.xaxis.set_major_formatter(majorFormatter)

        # for the minor ticks, use no labels; default NullFormatter
        ax1.xaxis.set_minor_locator(minorLocator)

        #plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Object Temperature over Time')
        plt.ylabel('Temperature (deg F)')

        #print(str(object_temp)[2:-1])
        #print(str(ambient_temp)[2:-1])
        #time.sleep(1)

    ani = animation.FuncAnimation(fig, animate, fargs=(xs1, ys1, ys2, kalman_filter_estimates), interval=1000)
    plt.show()

finally:
    p.disconnect()
