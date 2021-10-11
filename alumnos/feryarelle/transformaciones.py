from math import sin, cos
def fun(r, theta, fi):
    x= r*cos(fi)sin(theta)
    y= r*sin(fi)sin(theta)
    z= r*cos(theta)
    return (x, y, z)
