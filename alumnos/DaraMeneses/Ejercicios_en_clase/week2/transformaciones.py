from math import sin, cos
def esfericas(r,t,p):
    x= r*sin(t)*cos(p)
    y= r*sin(t)*sin(p)
    z= r*cos(t)
    return x, y, z

x, y, p = esfericas(1,5,1.1071487177940904)
print("La coordenada esférica es (",r,",",theta,",",phi,")")
