import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("lightsim_time_profile.csv",header=None)


fig = plt.figure()
ax = fig.add_subplot(111)

width=10
height=10
for i in range(data.shape[0]):

    rect=plt.Rectangle((data[1][i]-width,data[2][i]-height),2*width,2*height)
    ax.add_patch(rect)


plt.xlim(-1000,1000)
plt.ylim(-1000,1000)
plt.show()
