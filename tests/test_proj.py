import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, "../")

import particle.particle as pt

def exact_sol(x0, y0, v0, alpha0, t):
    v0x = v0 * np.cos(np.radians(alpha0))
    v0y = v0 * np.sin(np.radians(alpha0))
    x = x0 + v0x*t
    y = y0 + v0y*t - (0.5*pt.G)*t**2
    return x,y

x0, y0, v0, alpha0 = 0, 0.5, 1, 45

pluto = pt.Particle("Pluto",x0, y0, v0, alpha0)

x,y,vx,vy,t = pluto.get_state()

xposEuler = []
yposEuler = []
tpos = []

xposNum = []
yposNum = []

xposEuler.append(x)
yposEuler.append(y)
tpos.append(t)

x_error = []
y_error = []

while pluto.y >= 0:
    pluto.step(0.01)
    x,y,vx,vy,t = pluto.get_state()
    if pluto.y < 0: break
    xposEuler.append(x)
    yposEuler.append(y)
    tpos.append(t)

for t in tpos:
    xnum, ynum = exact_sol(x0, y0, v0, alpha0, t)
    xposNum.append(xnum)
    yposNum.append(ynum)

for i in range(0, len(yposNum)):
    err = abs(yposNum[i] - yposEuler[i])
    y_error.append(err)

for i in range(0, len(xposNum)):
    err = abs(xposNum[i] - xposEuler[i])
    x_error.append(err)

fig, ax = plt.subplots()
#ax.plot(tpos, yposEuler, '--', label = 'Numerical Solution')
#ax.plot(tpos, yposNum, '-', label = 'Exact Solution')
ax.plot(tpos, y_error, '-', label = "Error Y")
ax.plot(tpos, x_error, '--', label = "Error X")

ax.set(xlabel = "Time (s)", ylabel = "Errors", title = "Projectile Motion: Euler's Method")
ax.grid()

plt.show()
