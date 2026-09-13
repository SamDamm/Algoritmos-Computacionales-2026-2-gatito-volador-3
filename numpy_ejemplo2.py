import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

ang = np.arange(0, 720, 15)
x = np.radians(ang)
y= np.sin(x)
print(ang, x, y)
plt.plot(x, y, "-r")
plt.show()