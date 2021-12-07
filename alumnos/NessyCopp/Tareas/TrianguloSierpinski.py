
import numpy as np
import matplotlib.pyplot as plt

class TrianguloSierpinski:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def _generar(self, x1, y1, x2, y2, x3, y3, iteracion):
        
        if iteracion == 0:
            self.dibujar(x1, y1, x2, y2, x3, y3)
            
        elif iteracion >= 0:
            x12 = (x2 + x1)/2
            y12 = (y2 + y1)/2
            
            x13 = (x3 + x1)/2
            y13 = (y3 + y1)/2
            
            x23 = (x3 + x2)/2
            y23 = (y3 + y2)/2
            
            self._generar(x1, y1, x12, y12, x13, y13, iteracion - 1)
            self._generar(x13, y13, x3, y3, x23, y23, iteracion - 1)
            self._generar(x12, y12, x23, y23, x2, y2, iteracion - 1)
            
    def dibujar(self, x1, y1, x2, y2, x3, y3):
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], lw=1.0, color='blue')

    def generar(self, iteraciones=0):
        return self._generar(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, iteraciones)
