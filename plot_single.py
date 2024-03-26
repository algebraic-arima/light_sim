import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import animation

charge_sin=pd.read_csv("SPEWaveform_p.csv",encoding='utf-8',header=None)
position=pd.read_csv("lightsim_time_profile.csv",header=None)

charge_sin=np.array(charge_sin)
charge_sin=charge_sin[1]
position=np.array(position)

position_sin=position[0,1:3]
time=position[0,3:]


time=np.floor(time/0.2)
time=time[~np.isnan(time)]

time_total=np.arange(1,250001)*0.2
charge=np.zeros(250000)
count=-100
for i in range(time.shape[0]):
    count=count+int(time[i])
    charge[count:count+201]=charge[count:count+201]+charge_sin

plt.plot(time_total,charge)
plt.show()


fig, ax = plt.subplots()
update_counter = 0
def update(frame):
    global update_counter
    update_counter += 1
    rect = plt.Rectangle((0.25, 0.25), 0.5, 0.5, color=(1, 0, frame))
    ax.clear()
    ax.add_patch(rect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("t="+str(np.trunc(update_counter*0.2))+"ns")

ani = animation.FuncAnimation(fig, update, frames=10*charge+0.1, interval=0.02)
plt.show()


