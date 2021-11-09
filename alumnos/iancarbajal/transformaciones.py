import math
def spher(r,𝜃,𝜙):
    x=r*cos(𝜃)*sin(𝜙)
    y=r*sin(𝜃)*sin(𝜙)
    z=r*cos(𝜙)
    return (x,y,z)
def invspher(x,y,z):
    r=sqrt(x**2+y**2+z**2)
    𝜙=acos(z/r)
    𝜃=atan(y/x)
    return (r,𝜃,𝜙)
