from math import cos, sin
from ipywidgets import interact, fixed, widgets

def coo(rho,theta,omega):
    x = rho*cos(theta)*sin(theta)
    x = rho*sin(theta)*sin(theta)
    z = rho*cos(theta)
    return x, y, z

print(coo(5,70,6))
interact(coo, rho=5, theta=70, omega=6);
