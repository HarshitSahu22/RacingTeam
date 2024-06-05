import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"/Users/harshit/Desktop/RacingTeam/IITB_Racing_Elec_Trainees/Group 3/Harshit Sahu/Communications & Data Acquisition/CCD_file.csv")
data = pd.DataFrame(data)
data = data.dropna(how='all')

quant_yaw_rate = 0.005 #degree/s/digit
quant_yaw_ang_acc = 0.125 #degree/s^2/digit
quant_acc_X = 0.0001274 #g/digit
quant_acc_Y = 0.0001274 #g/digit
offset = 32768

data_112 = data[data['ID'] == 112].astype({'Data 0': int, 'Data 1': int, 'Data 2': int, 'Data 3': int, 'Data 4': int, 'Data 5': int, 'Data 6': int, 'Data 7': int})
data_128 = data[data['ID'] == 128].astype({'Data 0': int, 'Data 1': int, 'Data 2': int, 'Data 3': int, 'Data 4': int, 'Data 5': int, 'Data 6': int, 'Data 7': int})

a = np.ones(data_112['Data 1'].shape, dtype = int)*8

yaw_rate = np.array((((data_112['Data 1'] << a) | data_112['Data 0']) - 32768)*quant_yaw_rate)
yaw_acc_y = np.array((((data_112['Data 5'] << a) | data_112['Data 4']) - 32768)*quant_acc_Y*9.81)
yaw_ang_acc = np.array((((data_128['Data 1'] << a) | data_128['Data 0']) - 32768)*quant_yaw_ang_acc)
yaw_acc_x = np.array((((data_128['Data 5'] << a) | data_128['Data 4']) - 32768)*quant_acc_X*9.81)

fig,ax = plt.subplots(4,1,figsize=(10,15))

plt.subplot(4,1,1)
ax[0].plot(data_112['Time'][1:], yaw_rate[1:], color = 'r')
ax[0].set_title('Yaw Rate (degree/s) vs Time (s)')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Yaw Rate (degree/s)')

plt.subplot(4,1,2)
ax[1].plot(data_112['Time'][1:], yaw_ang_acc[1:], color = 'b')
ax[1].set_title('Angular Acceleration (degree s^-2) vs Time (s)')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Angular Acceleration (m s^-2)')

plt.subplot(4,1,3)
ax[2].plot(data_112['Time'][1:], yaw_acc_x[1:], color = 'black')
ax[2].set_title('Acceleration X (m s^-2) vs Time (s)')
ax[2].set_xlabel('Time (s)')
ax[2].set_ylabel('Acceleration X (m s^-2)')

plt.subplot(4,1,4)
ax[3].plot(data_128['Time'][1:], yaw_acc_y[1:])
ax[3].set_title('Acceleration Y (m s^-2) vs Time (s)')
ax[3].set_xlabel('Time (s)')
ax[3].set_ylabel('Acceleration Y (m s^-2)')

plt.tight_layout()
plt.show()