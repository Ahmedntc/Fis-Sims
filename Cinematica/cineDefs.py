import math
import numpy as np

def v_y(v0, ang):
  return v0 * math.sin(ang)

def speedY(v0, grav, time, ang):
  return v0 * math.sin(ang) - (grav * time)

def v_x(v0, ang):
  return v0 * math.cos(ang)

def V(v0, t , a):
  return v0 + t * a


def pos_X(p0_x, v_x, time):
  return p0_x + v_x * time

def pos_Y(p0_y, vI_y, time, grav):
  return p0_y + (vI_y * time) - (0.5 * grav * (time ** 2))

def v_T(v_x, v_y):
  return (math.sqrt(v_x ** 2  + v_y ** 2))

def anguloInst(vY, vX):
  return math.atan(vY/vX)

def forRes(d=0.47, p=1.21, a=0.8, v = 0.0):
    res = 0.5 * d * p * a * (v ** 2)
    return res

def aX(R, M, ang):
    return -(R * np.cos(ang))/M

def aY(R = 0.0, M = 0.0, G = 9.81, ang = 0.0):
    return -G-(R * np.sin(ang))/M