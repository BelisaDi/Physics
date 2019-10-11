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
    r_delta = r**(3+delta_sim)
    axp = -((GM*xp)/(r_delta))
    ayp = -((GM*yp)/(r_delta))
    return vxp, vyp, axp, ayp, 1.

def euler_cromer(planet, numeric, xpos, ypos, tpos, angles):
    for i in range(6260):
        xc, yc, _, _, tc = planet.get_state()
        xpos.append(xc)
        ypos.append(yc)
        tpos.append(tc)
        ang = planet.get_angle()/np.pi
        #ang_inicial = planet.get_angle()
        angles.append(ang)
        numeric.euler_cromer_step(deltat)
        #ang_final = planet.get_angle()
        #angles.append((ang_final - ang_inicial)/deltat)

#Initial Variables and lists
#np.sqrt((pt.GM)/1**(1+delta_sim))
deltat = 0.001
delta_sim = 0.1
m, x0, y0, v0, a0 = 1., 1., 0., 5, 90
sim_params = pt.GM, delta_sim

planet2 = pt.Particle("Planet Y", x0, y0, v0, a0, m)
planet2.set_force(fr.Forces(grav_force, sim_params))

xposEulerCromer = []
yposEulerCromer = []
tposEulerCromer = []
angles = []
graph_angles = []
graph_time = []

numeric2 = sv.Solver(planet2, "Euler-Cromer", deltat)
euler_cromer(planet2, numeric2, xposEulerCromer, yposEulerCromer, tposEulerCromer, angles)

val = True
cont = 0
time = 0
for i in range(len(angles)):
    if(val == True):
        graph_angles.append(angles[i])
        graph_time.append(time)
        val = False
    else:
        if(cont == 626):
            time += 1
            graph_angles.append(angles[i])
            graph_time.append(time)
            cont = 0
        cont += 1
print(len(angles))
print(len(graph_angles))

differences = []
for i in range(len(graph_angles) - 1):
    differences.append(graph_angles[i+1] - graph_angles[i])

average = sum(differences)/len(differences)
print(graph_angles)
print(differences)
print(average)
#Generate Plots

fig, ax = plt.subplots()

ax.plot(graph_time, graph_angles, 'ro')
#ax.plot(xposEulerCromer, yposEulerCromer, '-')

ax.set(xlabel='time (yr)', ylabel='Angle per revolution',
       title='Delta = 0.1 and 6260 iterations')
ax.grid()

plt.legend()
plt.show()
