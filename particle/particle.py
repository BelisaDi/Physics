# coding: utf-8

import numpy as np

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
if __name__ == "__main__":
  mars = Particle("Mars",1,2,100,60)
  print(mars)
