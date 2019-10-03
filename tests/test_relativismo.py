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
    GM, delta_sim = params
    r = np.sqrt(xp**2 + yp**2)
    r_delta = r**(2+delta_sim)
    axp = -((GM*xp)/(r_delta*r))
    ayp = -((GM*yp)/(r_delta*r))
    return vxp, vyp, axp, ayp, 1.

def euler_cromer(planet, numeric, xpos, ypos, tpos, angles):
    for i in range(40000):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        #ang = planet.get_angle()/np.pi
        ang_inicial = planet.get_angle()
        #angles.append(ang)
        numeric.euler_cromer_step(deltat)
        ang_final = planet.get_angle()
        angles.append((ang_final - ang_inicial)/deltat)

#Initial Variables and lists
#np.sqrt((pt.GM)/1**(1+delta_sim))
deltat = 0.0001
delta_sim = 0.05
m, x0, y0, v0, a0 = 1., 1., 0., 5, 90
sim_params = pt.GM, delta_sim

planet2 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet2.set_force(fr.Forces(grav_force, sim_params))

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []
angles = []
graph_angles = []

numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)

euler_cromer(planet2, numeric2, xposEulerCromer, yposEulerCromer, tposEulerCromer, angles)


#Generate Plots

fig, ax = plt.subplots()
#print(angles)

ax.plot(tposEulerCromer, angles, '-', label='Euler-Cromer')
#ax.plot(xposEulerCromer, yposEulerCromer, '-')

ax.set(xlabel='time', ylabel='angle',
       title='First trial')
ax.grid()

plt.legend()
plt.show()
