import numpy as np
import math
import matplotlib.pyplot as plt

v_0 = 100 
ang = math.radians(60)
vx_0 = v_0 * math.cos(ang)
vy_0 = v_0 * math.sin(ang)
ay = -9.8
y0 = 0
x0 = 0

n = 1000
pos_x = np.zeros(n)
pos_y = np.zeros(n)

t = 0
t_max = 100
dt = (t_max - t) / n 

vy = vy_0
x = x0
y = y0 

i = 0
while t < t_max and y >= 0 :
    vy = vy + ay * dt
    y = y + vy * dt
    x = x + vx_0 * dt

    pos_x[i] = x
    pos_y[i] = y

    t += dt
    i += 1

print (pos_x[:i], pos_y[:i])
plt.plot(pos_x[:i-1], pos_y[:i-1], "g-")
plt.show()
 