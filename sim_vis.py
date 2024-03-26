import numpy as np
import matplotlib.pyplot as plt
import csv

test = []
time_max = 0

patch_arrival = {}
# map from time to index

pulse_time = []
pulse_vol = []

with open("SPEWaveform.csv", "r") as file_aux:
    reader = csv.reader(file_aux)
    for row in reader:
        pulse_time.append(float(row[0]))
        pulse_vol.append(float(row[1]))

for i in range(2304):
    test.append(np.around(np.load(f'result_arrival/patch_{i}.npy'), 10))
    for j in test[i]:
        tmp_ind = int(j * 1e10)
        for k in range(50):
            if tmp_ind not in patch_arrival:
                patch_arrival[tmp_ind] = []
            if k % 2 == 0:
                patch_arrival[tmp_ind].append((i, pulse_vol[int(101 + k / 2)]))
            else:
                patch_arrival[tmp_ind].append((i, (pulse_vol[int(101 + k / 2) + 1] + pulse_vol[int(101 + k / 2)]) / 2))
            tmp_ind += 1
    time_max = max(time_max, np.max(test[i]))

# for i in range(50001):


# print(test[0])
# num = len(test[0])
# print(test[0])

# plt.plot(np.linspace(0, num * simu_interval, num=num, endpoint=False), np.transpose(test[0][:num]))
# plt.show()

x = np.load('result/a_x_accords.npy')
y = np.load('result/a_y_accords.npy')

xmax = max(x)
ymax = max(y)
xmin = min(x)
ymin = min(y)

fig, ax = plt.subplots()
y1 = []

for k in range(2304):
    rect = plt.Rectangle((int(x[k]), int(y[k])), 20, 20, color=(0, 0, 0))
    ax.add_patch(rect)
ax.set_xlim(xmin - 50, xmax + 50)
ax.set_ylim(ymin - 50, ymax + 50)
plt.pause(10)
i = 0
while i <= 1000:
    ax.clear()
    # for k in range(2304):
    #     rect = plt.Rectangle((int(x[k]), int(y[k])), 5, 5, color=(1, 1, 1))
    #     ax.add_patch(rect)

    if i in patch_arrival:
        for j in patch_arrival[i]:
            col = min(max(0, j[1] / 0.05), 1)
            rect = plt.Rectangle((int(x[j[0]]), int(y[j[0]])), 20, 20, color=(1, 1 - col, 1 - col))
            ax.add_patch(rect)
    ax.set_xlim(xmin - 2, xmax + 2)
    ax.set_ylim(ymin - 2, ymax + 2)
    ax.set_title("t=" + str(np.trunc(i * 0.1)) + "ns")
    plt.pause(0.0001)
    i += 1
