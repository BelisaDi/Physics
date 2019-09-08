import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, "../")
import particle.particle as pt

#Function Definitions

def exact_sol(x0, y0, v0, alpha0, t):
    v0x = v0 * np.cos(np.radians(alpha0))
    v0y = v0 * np.sin(np.radians(alpha0))
    x = x0 + v0x*t
    y = y0 + v0y*t - (0.5*pt.G)*t**2
    return x,y

def euler(particle, xlist, ylist, tlist):
    while particle.y >= 0:
        particle.euler_step(0.01, 4)
        x,y,vx,vy,t = particle.get_state()
        if particle.y < 0: break
        xlist.append(x)
        ylist.append(y)
        tlist.append(t)

def euler_cromer(particle, xlist, ylist, tlist):
    while particle.y >= 0:
        particle.euler_cromer_step(0.01, 4)
        x,y,vx,vy,t = particle.get_state()
        if particle.y < 0: break
        xlist.append(x)
        ylist.append(y)
        tlist.append(t)

#Initial Variables and Lists

x0, y0, v0, alpha0 = 0, 0.5, 1, 45
pluto = pt.Particle("Pluto",x0, y0, v0, alpha0)
pluto2 = pt.Particle("Pluto 2",x0, y0, v0, alpha0)
x,y,vx,vy,t = pluto.get_state()

xposEuler = []
yposEuler = []
tpos = []

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []

xposNum = []
yposNum = []

xposEuler.append(x)
yposEuler.append(y)
tpos.append(t)

xposEulerCromer.append(x)
yposEulerCromer.append(y)
tposEulerCromer.append(t)

x_error = []
y_error = []

#Execution of Numerical Methods and Exact Solutions
euler(pluto, xposEuler, yposEuler, tpos)
euler_cromer(pluto2, xposEulerCromer, yposEulerCromer, tposEulerCromer)

for t in tpos:
    xnum, ynum = exact_sol(x0, y0, v0, alpha0, t)
    xposNum.append(xnum)
    yposNum.append(ynum)

#Error calculations
for i in range(0, len(yposNum)):
    err = abs(yposNum[i] - yposEuler[i])
    y_error.append(err)

for i in range(0, len(xposNum)):
    err = abs(xposNum[i] - xposEuler[i])
    x_error.append(err)

#Plotting the results
fig, ax = plt.subplots()
ax.plot(xposEulerCromer, yposEulerCromer, '--', label = 'Euler Cromer Solution')
ax.plot(xposEuler, yposEuler, '-', label = 'Euler Solution')
#ax.plot(tpos, y_error, '-', label = "Error Y")
#ax.plot(tpos, x_error, '--', label = "Error X")

ax.set(xlabel = "X Position", ylabel = "Y Position", title = "Projectile Motion: Euler's Methods")
ax.grid()

plt.show()
