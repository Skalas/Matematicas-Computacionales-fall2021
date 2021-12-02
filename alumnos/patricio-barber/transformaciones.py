import math

def polar_cart(r, theta, phi):
    """
    r=distancia radial
    theta=ángulo polar
    phi= azimut
    """
    return [r * math.sin(theta) * math.cos(phi),r * math.sin(theta) * math.sin(phi), r * math.cos(theta)]
