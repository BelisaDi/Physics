import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, "../")

import particle.particle as pt
import forces.forces as fr
import solver.solver as sv

#Function Definitions

def grav_force(state, params):
    xp, yp, vxp, vyp, _ = state
    GM = params
    r2 = xp**2 + yp**2
    r3 = r2*np.sqrt(r2)
    axp = -((GM*xp)/r3)
    ayp = -((GM*yp)/r3)
    return vxp, vyp, axp, ayp, 1.

def euler_cromer(planet, numeric, xpos, ypos, tpos, vel):
    for i in range(16800):
        xc, yc, vxc, vyc, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        vel.append(np.sqrt(vxc**2 + vyc**2))
        numeric.euler_cromer_step(deltat)

#Initial Variables and lists

m, x0, y0, v0, a0 = 1., 0.5, 0., 4., 90
deltat = 0.001
sim_params = pt.GM

planet2 = pt.Particle("Planet X", x0, y0, v0, a0, m)
planet_force = fr.Forces(grav_force, sim_params)
planet2.set_force(planet_force)

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []
vel = []

numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)

euler_cromer(planet2, numeric2, xposEulerCromer, yposEulerCromer, tposEulerCromer, vel)

#Generate Plots
#print(xposEulerCromer)
print("Xs")
xmax = max(xposEulerCromer)
xmin = min(xposEulerCromer)
print(xmax)
print(xmin)
print("Ys")
#print(yposEulerCromer)
ymax = max(yposEulerCromer)
ymin = min(yposEulerCromer)
print(ymax)
print(ymin)

fig, ax = plt.subplots()
ax.plot(xposEulerCromer, yposEulerCromer, '-', label='Euler-Cromer')
#ax.plot(yposEulerCromer, vel, '-', label='Euler-Cromer')

ax.set(xlabel='t yr', ylabel='vel',
       title='Ensayo y error ')
ax.grid()

plt.legend()
plt.show()
