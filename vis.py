import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

test = []

for i in range(100):
    test.append(np.load(f'result/signal_{i}.npy')[0])

# print(test[0])
# num = len(test[0])
# print(test[0])
simu_interval = 2e-10
num = 2000
# plt.plot(np.linspace(0, num * simu_interval, num=num, endpoint=False), np.transpose(test[0][:num]))
# plt.show()

x = np.load('result/a_x_accords.npy')
y = np.load('result/a_y_accords.npy')

pointnum = 1
timemax = 1000

xmax = max(x[:pointnum])
ymax = max(y[:pointnum])
xmin = min(x[:pointnum])
ymin = min(y[:pointnum])

fig, ax = plt.subplots()
y1 = []
i = 0
while i <= 1000:
    ax.clear()
    for j in range(pointnum):
        reg = abs(test[0][i]) / max(test[0])
        if reg <= 1e-1:
            continue
        rect = plt.Rectangle((int(x[j]), int(y[j])), 0.5, 0.5, color=(1 - reg, 1 - reg, 1 - reg))
        ax.add_patch(rect)
    ax.set_xlim(xmin - 2, xmax + 2)
    ax.set_ylim(ymin - 2, ymax + 2)
    ax.set_title("t=" + str(np.trunc(i * 0.2)) + "ns")
    plt.pause(0.0000001)
    i += 1
