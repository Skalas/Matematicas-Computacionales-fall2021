from math import sqrt, atan, acos
def esfericas(x,y,z):
    r= sqrt(x^2+y^2+z^2)
    theta= z/r
    phi= atan(y/x)
    return r, theta, phi
