import math
import numpy as np

file = open("data.txt", "w+")

for i in np.linspace(0, 1, int(input("Enter number of elements: "))):
    file.writelines(str(math.cos(2*math.pi*2000*i))+"\n")