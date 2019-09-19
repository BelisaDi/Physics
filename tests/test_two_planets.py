import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, "../")

import particle.particle as pt
import forces.forces as fr

#Function Definitions

def grav_force(state, params):
    xp, yp, vxp, vyp, rp, _ = state
    mass, grav = params
    axp = -((grav*mass)/rp**3)*xp
    ayp = -((grav*mass)/rp**3)*yp
    return vxp, vyp, axp, ayp, 1.

def euler(planet, xpos, ypos, tpos):
    for i in range(630):
        xc, yc, _, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        planet.euler_step(deltat)

def euler_cromer(planet, xpos, ypos, tpos):
    for i in range(100000):
        xc, yc, _, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        planet.euler_cromer_step(deltat)

def midpoint(planet, xpos, ypos, tpos):
    for i in range(630):
        xc, yc, _, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        planet.midpoint_step(deltat)

#Initial Variables and lists

m1, x01, y01, v01, a01 = 1., 1., 0., 0.316227766, 90
m2, x02, y02, v02, a02 = 1., 2., 1., 0.5, 90
deltat = 0.01
sim_params = pt.M, pt.G

planet1 = pt.Particle("Planet X", x01, y01, v01, a01, m1)
planet1_force = fr.Forces(grav_force, sim_params)
planet1.set_force(planet1_force)

planet2 = pt.Particle("Planet Y", x02, y02, v02, a02, m2)
planet2_force = fr.Forces(grav_force, sim_params)
planet2.set_force(planet2_force)

xpos1 = []
ypos1 = []
tpos1 = []

xpos2 = []
ypos2 = []
tpos2 = []

euler_cromer(planet1, xpos1, ypos1, tpos1)
euler_cromer(planet2, xpos2, ypos2, tpos2)

#Generate Plots

fig, ax = plt.subplots()
ax.plot(xpos1, ypos1, '-', label='Planet X')
ax.plot(xpos2, ypos2, '--', label='Planet Y')

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='A first try to planet motion')
ax.grid()

plt.legend()
plt.show()
