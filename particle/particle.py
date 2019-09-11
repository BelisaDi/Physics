# coding: utf-8

import numpy as np

G = 1.
DRAG = 4.

class Particle:

    def __init__(self, label, x0, y0, v0, alpha0, m0 = 1, t0 = 0):
        self.lb = label
        self.x, self.y = x0, y0
        self.vx = v0 * np.cos(np.radians(alpha0))
        self.vy = v0 * np.sin(np.radians(alpha0))
        self.m, self.t = m0, t0
        self.force = None

    def __str__(self):
        string = self.lb + "\n"
        string += "mass = {}, time = {}\n".format(self.m, self.t)
        string += "position = ({:.4f}, {:.4f})\n".format(self.x, self.y)
        string += "velocity = ({:.4f}, {:.4f})\n".format(self.vx, self.vy)
        return string

    def euler_step(self, dt):
        state = self.x, self.y, self.vx, self.vy, self.t
        dxdt, dydt, dvxdt, dvydt, dtdt = self.force.get_force(state)
        self.x = self.x + dxdt * dt
        self.y = self.y + dydt * dt
        self.vx = self.vx + dvxdt * dt
        self.vy = self.vy + dvydt * dt
        self.t = self.t + dtdt * dt

    def euler_cromer_step(self, dt):
        state = self.x, self.y, self.vx, self.vy, self.t
        dxdt, dydt, dvxdt, dvydt, dtdt = self.force.get_force(state)
        self.vx = self.vx + dvxdt * dt
        self.vy = self.vy + dvydt * dt
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        self.t = self.t + dtdt * dt

    def midpoint_step(self, dt):
        state = self.x, self.y, self.vx, self.vy, self.t
        dxdt, dydt, dvxdt, dvydt, dtdt = self.force.get_force(state)
        vx_old, vy_old = self.vx, self.vy
        self.vx = self.vx + dvxdt * dt
        self.vy = self.vy + dvydt * dt
        self.x = self.x + (0.5) * (vx_old + self.vx) * dt
        self.y = self.y + (0.5) * (vy_old + self.vy) * dt
        self.t = self.t + dtdt * dt

    def get_state(self):
        return self.x, self.y, self.vx, self.vy, self.t

    def set_force(self, netforce):
        self.force = netforce
