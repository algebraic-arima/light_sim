import csv

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.interpolate import interp1d

# from here reads the time that light arrives
with open("lightsim_time_profile.txt", "r") as file:
    lines = file.readlines()

data_dict = {}

for line in lines:
    items = line.strip().split()
    key = tuple(map(float, items[:3]))
    value = tuple(map(float, items[3:]))
    data_dict[key] = value

x_accords = []
y_accords = []

for key in data_dict:
    x_accords.append(key[1])
    y_accords.append(key[2])

np.save("result/a_x_accords.npy", x_accords)
np.save("result/a_y_accords.npy", y_accords)

plt.scatter(x_accords, y_accords, s=10, marker='s')
plt.show()

time = {}
# time is a map from index to the time that light arrives
max_time = 0
for key in data_dict:
    time[int(key[0])] = np.cumsum(list(data_dict[key])) / 1E9
    max_time = max(max_time, max(time[int(key[0])]))
    np.save("result_arrival/patch_" + str(int(key[0])) + ".npy", time[int(key[0])])

# end

# from here reads the voltage of every pulses

pulse_time = []
pulse_vol = []

print(max_time)

with open("SPEWaveform.csv", "r") as file_aux:
    reader = csv.reader(file_aux)
    for row in reader:
        pulse_time.append(float(row[0]))
        pulse_vol.append(float(row[1]))

print(len(pulse_vol))
# plt.plot(pulse_time, pulse_vol)
# plt.show()

# end

# from here sums the voltages together

# signal = {}
# tot_interval = 5e-5
# simu_interval = 2e-10
# num = int(tot_interval / simu_interval)
# print(num)
# print(time[1785])
# # time, pulse_time, pulse_vol
# for k in range(2304):
#     tmp_time = time[k]
#     tmp = np.zeros((1, num))
#     cnt = 0
#     stack = []
#     for i in range(num):
#         while (len(stack) != 0) and (i * simu_interval > tmp_time[stack[0]] + 1.90e-8):
#             stack.pop(0)
#         while (cnt < len(tmp_time)) and (i * simu_interval >= tmp_time[cnt] - 1.98e-8):
#             stack.append(cnt)
#             cnt += 1
#         for j in range(len(stack)):
#             tmp[0, i] += pulse_vol[i - round(int((tmp_time[stack[j]] - 2.02e-8) / simu_interval))]
#     # signal[k] = tmp
#     # print(tmp)
#     # print('%6f' % float(tmp[0][0]))
#     np.save(f"result/signal_{k}.npy", tmp)
