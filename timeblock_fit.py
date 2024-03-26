import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

block_v_num = np.load('num_v_result/block_vnum_200ns.npy')

pos = [np.load('result/a_x_accords.npy'), np.load('result/a_y_accords.npy')]


def func1(r, a, z_0, r_x, r_y):
  ans = a * z_0 * (z_0 ** 2 + (r[0] - r_x) ** 2 + (r[1] - r_y) ** 2) ** (-1.5)
  return ans


fit_pos = []

for i in range(100):
  fit_pos.append(curve_fit(func1, pos, block_v_num[:, i])[0][2:4])

fit_pos = np.array(fit_pos)
print(np.cov(np.transpose(fit_pos)))

plt.scatter(fit_pos[:, 0], fit_pos[:, 1])
plt.xlim([-100, 100])
plt.ylim([-100, 100])
plt.show()
