import numpy as np
import matplotlib.pyplot as plt

test = []
time_max = 0

# map from time to index

block_vnum = []
vmax = 0

for i in range(2304):
  test = np.load(f'result_arrival/patch_{i}.npy')
  tmp = np.zeros([1, 250])
  for j in test:
    tmp[0][int(j * 1e9 / 200)] += 1
  block_vnum.append(tmp[0])
  vmax = max(vmax, max(tmp[0]))

np.save('num_v_result/block_vnum_200ns.npy', block_vnum)

weighted_sum_x = np.zeros([1, 250])
weighted_sum_y = np.zeros([1, 250])
sum = np.zeros([1, 250])

x = np.load('result/a_x_accords.npy')
y = np.load('result/a_y_accords.npy')

for i in range(2304):
  weighted_sum_x += block_vnum[i] * x[i]
  weighted_sum_y += block_vnum[i] * y[i]
  sum += block_vnum[i]

sum = sum[0][0:239]
weighted_sum_x = weighted_sum_x[0][0:239]
weighted_sum_y = weighted_sum_y[0][0:239]

weighted_sum_x = weighted_sum_x / sum
weighted_sum_y = weighted_sum_y / sum

plt.scatter(weighted_sum_x, weighted_sum_y)
plt.show()

# 5e4ns,200,250

# for i in range(50001):


# print(test[0])
# num = len(test[0])
# print(test[0])

# plt.plot(np.linspace(0, num * simu_interval, num=num, endpoint=False), np.transpose(test[0][:num]))
# plt.show()


#
# xmax = max(x)
# ymax = max(y)
# xmin = min(x)
# ymin = min(y)
#
# fig, ax = plt.subplots(1, 1, figsize=(50, 50))
#
# for k in range(2304):
#     rect = plt.Rectangle((int(x[k]), int(y[k])), 20, 20, color=(0, 0, 0))
#     ax.add_patch(rect)
# ax.set_xlim(xmin - 50, xmax + 50)
# ax.set_ylim(ymin - 50, ymax + 50)
# i = 0
# while i < 250:
#     ax.clear()
#     # for k in range(2304):
#     #     rect = plt.Rectangle((int(x[k]), int(y[k])), 5, 5, color=(1, 1, 1))
#     #     ax.add_patch(rect)
#
#     for j in range(2304):
#         col = min(max(0, block_vnum[j][i] / vmax), 1)
#         rect = plt.Rectangle((int(x[j]), int(y[j])), 20, 20, color=(1, 1 - col, 1 - col))
#         ax.add_patch(rect)
#     ax.set_xlim(xmin - 2, xmax + 42)
#     ax.set_ylim(ymin - 2, ymax + 42)
#     ax.set_aspect('equal')
#     ax.set_title("t=" + str(i * 200) + "ns-" + str(i * 200 + 200) + "ns", fontsize=50)
#     plt.savefig(f'num_v_result/num_v{i}.png')
#     i += 1

# http://lic.si.sjtu.edu.cn:9080
