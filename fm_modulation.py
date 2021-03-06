import numpy as np
import matplotlib.pyplot as mpl
import math

file_name = input("Enter File Name: ")
file_handle = open(file_name, "r")

input_signal = []

for point in file_handle:
    input_signal.append(float(point))

input_signal = np.array(input_signal)

mp = min(input_signal)
deviation_ratio = float(input("Enter value of deviation ratio: "))
fc = float(input("Enter value of carrier frequency: "))
time_gaps = 1 / (2*fc)
number_of_input_points = len(input_signal)
time_vector = np.linspace(0, 1, number_of_input_points)

carrier_signal = np.cos(2*np.pi*fc*time_vector)
output_signal = np.cos(2*np.pi*fc + deviation_ratio*input_signal)

mpl.subplot(3,1,1)
mpl.title('Frequency Modulation')
mpl.plot(input_signal,'g')
mpl.ylabel('Amplitude')
mpl.xlabel('Input signal')

mpl.subplot(3,1,2)
mpl.plot(carrier_signal, 'r')
mpl.ylabel('Amplitude')
mpl.xlabel('Carrier signal')

mpl.subplot(3,1,3)
mpl.plot(output_signal, color="purple")
mpl.ylabel('Amplitude')
mpl.xlabel('Output signal')

mpl.subplots_adjust(hspace=1)
mpl.rc('font', size=30)

mpl.show()