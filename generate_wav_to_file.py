from scipy.io.wavfile import read
from scipy.signal import decimate

import numpy

print("Press 1 for PinkPanther60.wav")
print("Press 2 for CantinaBand3.wav")
opt = int(input("Enter option: "))

if opt == 1:
    wav_file = read("assets/PinkPanther60.wav")
else:
    wav_file = read("assets/CantinaBand3.wav")
    
wav_array = numpy.array(wav_file[1], dtype=float)
wav_array = decimate(wav_array, 50)

file = open("data.txt", "w+")

for i in wav_array:
    file.writelines(str(i) + "\n")