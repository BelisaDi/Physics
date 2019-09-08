# coding: utf-8

import numpy as np

G = 1

class Particle:

    def __init__(self, label, x0, y0, v0, alpha0, m0 = 1, t0 = 0):
        self.lb = label
        self.x, self.y = x0, y0
        self.vx = v0 * np.cos(np.radians(alpha0))
        self.vy = v0 * np.sin(np.radians(alpha0))
        self.m = m0
        self.t = t0

    def __str__(self):
        string = self.lb + "\n"
        string += "mass = {}, time = {}\n".format(self.m, self.t)
        string += "position = ({:.4f}, {:.4f})\n".format(self.x, self.y)
        string += "velocity = ({:.4f}, {:.4f})\n".format(self.vx, self.vy)
        return string

    def euler_step(self, dt, c):
        #This is with F = -mg
        # self.x = self.x + dt*self.vx
        # self.y = self.y + dt*self.vy
        # self.vx = self.vx
        # self.vy = self.vy -(dt*G)
        # self.t = self.t + dt

        #This is with F = mg + cV (drag resistance)
        self.x = self.x + dt*self.vx
        self.y = self.y + dt*self.vy
        self.vx = self.vx*(1 - (c/self.m)*dt)
        if self.vy >= 0:
            self.vy = self.vy*(1 - (dt*c)/self.m) - dt*G
        else:
            self.vy = self.vy*(1 + (dt*c)/self.m) - dt*G
        self.t = self.t + dt

    def euler_cromer_step(self, dt, c):
        #This is with F = -mg
        # self.vx = self.vx
        # self.vy = self.vy -(dt*G)
        # self.x = self.x + dt*self.vx
        # self.y = self.y + dt*self.vy
        # self.t = self.t + dt

        #This is with F = mg + cV (drag resistance)
        self.vx = self.vx*(1 - (c/self.m)*dt)
        if self.vy >= 0:
            self.vy = self.vy*(1 - (dt*c)/self.m) - dt*G
        else:
            self.vy = self.vy*(1 + (dt*c)/self.m) - dt*G
        self.x = self.x + dt*self.vx
        self.y = self.y + dt*self.vy
        self.t = self.t + dt

    def get_state(self):
        return self.x, self.y, self.vx, self.vy, self.t


if __name__ == "__main__":
  mars = Particle("Mars",1,2,100,60)
  print(mars)
