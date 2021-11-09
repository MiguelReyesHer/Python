""" 
Este programa de Python permite resolver el problema 4 del examen: Contaminación del aire.
Creado el 04 de noviembre del 2021
@autor: MARH

Problema: 
Entre 1850 y 1985, aproximadamente 155,000 millones de toneladas métricas de carbón se descargaron en la atmósfera terrestre y el clima se hizo 0.5°C 
más caliente, indicación ésta del efecto invernadero. Se estima que duplicar la cantidad de CO2 en la atmósfera resultaría en un aumento promedio de 
la temperatura mundial de 4° a 5°C. La cantidad futura A de CO2 en la atmósfera en partes por millón a veces se calcula usando la fórmula: 
A = a + ct + ke^(rt), donde a, c y k son constantes, r es el porcentaje de aumento en la emisión de CO2 y t es el tiempo en años, con t=0 correspondiente 
a 1990. Suponga que se calcula que en el año 2070, A será 800, si r=2.5% y A será 560 si r=1.5%. Si, en 1990 A=340 y r=1%, encuentre el año en el que 
la cantidad de CO2 en la atmósfera se habrá multiplicado. 

Sistema de ecuaciones derivado del problema planteado:
a + 80c + 7.39k = 800
a + 80c + 3.32k = 560
a       +     k = 340
"""

from matplotlib import pyplot#Permite mostrar gráficos
from math import e#Obtenemos el número de Euler
import numpy as np#Permite realizar operaciones con matrices.
#Si muestra un error, instalar la librería desde su dispositivo, en su terminal agregue el comando "pip install (Librería)"

#Procedimiento parte 1: Hallar el valor de las constantes del sistema de ecuaciones

#Definimos la matriz de coeficientes del S.E.
A = np.matrix([ [1,80,7.39],[1,80,3.32],[1,0,1] ])

#Se define el vector solución
SOLA = np.matrix([ [800],[560],[340] ])

#Se resuelve el sistema de ecuaciones
XA = np.linalg.solve(A,SOLA)

#Se imprime la primera parte de la respuesta 
print(f"\nConsiderando que a, c y k tienen los valores:\n{XA}\nPara A = a + ct + ke^(rt),")

#Procedimiento parte 2: Graficar la función

#Se define la función, reemplazando los valores de a, c y k del procedimiento 1 en la fórmula A = a + ct + ke^(rt)
def f1(t):
    return 281.03 + (1.039*t) + (58.96 * (e**(0.02*t)))

#Valores a evaluar que toma el eje x (t) en el gráfico (El dominio)
t = range(0,100)

#Graficar
pyplot.plot(t, [f1(i) for i in t])

#Etiquetas
pyplot.title("Contaminación del aire",#Título de la gráfica
          fontdict={'color' : 'red',
                    'weight': 'bold',
                    'size': 26})
pyplot.xlabel("Años", size = 16)#Eje X
pyplot.ylabel("PPM CO2", size = 16)#Eje Y
pyplot.grid()#Mostrar cuadrícula en la gráfica

#Limitamos los valores de los ejes
pyplot.xlim(0, 100)#Dominio
pyplot.ylim(0, 800)#Rango

#Guardar el gráfico como imágen PNG
pyplot.savefig("output.png")

#Resultado final
print(f"y tomando en cuenta la gráfica de la función, el año donde A=680 y r=2%, es: {1990+83}")

#Mostrar la gráfica
pyplot.show()