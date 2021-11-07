from math import sqrt, atan

def coor_esf(x,y,z):
    r=sqrt(x**2+y**2+z**2)
    theta = atan(y/x)
    fi = sqrt(x**2+y**2)/z
    return r, theta, fi
