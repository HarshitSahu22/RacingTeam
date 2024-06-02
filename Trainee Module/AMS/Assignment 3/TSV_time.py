import pandas as pnd
import matplotlib.pyplot as plot
import numpy as np

file=pnd.read_csv(r"/Users/harshit/Desktop/Racing/HarshitSahu/AMS/Assignment 3/AMSCelldata97.csv")
input=file['TSV']

print(input.mean())

x=np.linspace(0,3476,34758)

plot.plot(x,input)

plot.xlabel('Time')
plot.ylabel('Tractive Sysytem Voltage')

plot.legend()

plot.show()