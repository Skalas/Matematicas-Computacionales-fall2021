def cilindro(r,theta,fi):
    x=r*np.sin(theta)*np.cos(fi)
    y=r*np.sin(fi)*np.sin(theta)
    z=r*np.cos(theta)
    return x,y,z
