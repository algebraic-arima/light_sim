import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("SPEWaveform.csv",encoding='utf-8',header=None)
print(data)

plt.plot(data[0],data[1],linewidth=1.5)
plt.scatter(data[0],data[1],c="maroon",s=6)
plt.show()

