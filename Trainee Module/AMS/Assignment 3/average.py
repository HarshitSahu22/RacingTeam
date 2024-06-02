import numpy as np
import pandas as pnd
import matplotlib.pyplot as plot

file=pnd.read_csv(r"/Users/harshit/Desktop/Racing/HarshitSahu/AMS/Assignment 3/AMSCelldata97.csv")

x=np.linspace(1,90,90)
y=file.iloc[:,x-1].mean()

plot.bar(x,y)

file['Power'] = file['TSC']*file['TSV']
avg_power = abs(file['Power']).mean()

print(f'The average power is {avg_power:.2f} Watts')

plot.xlabel('Cell Index')
plot.ylabel('Average Cell Voltage')

plot.show()