import numpy as np
import matplotlib.pyplot as plt

#La clase define in objeto del tipo par ordenado, que se inicializa
#con sus componentes a y b, de la forma binómica de un número complejo:
#(a+ib)
class ParOrdenado:
    def __init__(self,a,b):
        self.real = int(a)
        self.imaginario = int(b)

#La funcion graficar se supone debe tomar esos valores y usarlos para 
#crear un vector que vaya de 0 a el componente respectivo de X y Y
def graficarComp(e):
    # Coordenadas del vector
    x, y = e.real, e.imaginario

    # Limites de la figura
    izda = min(-1, x-1)
    dcha = max(1, x+1)
    abajo = min(-1, y-1)
    arriba = max(1, y+1)

    # El metodo quiver pinta vectores, pero para que salgan de las
    # dimensiones correctas hay que usar los parámetros angles, scale y scale_units

    plt.quiver([x], [y], angles='xy', scale_units='xy', scale=1)

    # Pintamos lineas que pasan por el origen de coordenadas
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Fijamos límites, etiquetas y títulos
    plt.xlim([izda, dcha])
    plt.ylim([abajo, arriba])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('({},{})'.format(e.real,e.imaginario))
    plt.show()
    
ejemplo = ParOrdenado(3,6)
graficarComp(ejemplo)