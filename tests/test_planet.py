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
    for i in range(630):
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

m, x0, y0, v0, a0 = 1., 1., 0., 0.316227766, 90
deltat = 0.01
sim_params = pt.M, pt.G

planet = pt.Particle("Planet X", x0, y0, v0, a0, m)
planet_force = fr.Forces(grav_force, sim_params)
planet.set_force(planet_force)

planet2 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet2.set_force(planet_force)

planet3 = pt.Particle("Planet Z", x0, y0, v0, a0, m)
planet3.set_force(planet_force)

xposEuler = []
yposEuler = []
tposEuler = []

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []

xposMidpoint = []
yposMidpoint = []
tposMidpoint = []

euler(planet, xposEuler, yposEuler, tposEuler)
euler_cromer(planet2, xposEulerCromer, yposEulerCromer, tposEulerCromer)
midpoint(planet3, xposMidpoint, yposMidpoint, tposMidpoint)

#Generate Plots

fig, ax = plt.subplots()
ax.plot(xposEuler, yposEuler, '-', label='Euler')
ax.plot(xposEulerCromer, yposEulerCromer, '--', label='Euler-Cromer')
ax.plot(xposMidpoint, yposMidpoint, '--', label='Midpoint')

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='A first try to planet motion')
ax.grid()

plt.legend()
plt.show()
