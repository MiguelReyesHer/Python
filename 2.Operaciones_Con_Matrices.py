""" 
Este programa de Python permite realizar operaciones entre matrices.
Creado el 30 de octubre del 2021
Autor MARH 
"""

import numpy as np #Importamos la librería numpy para realizar cálculos entre matrices.
#Si muestra un error, instalar numpy desde su dispositivo, en su terminal agregar el comando "pip install numpy"

#Defnimos las matrices con las que operaremos
A = np.matrix([ [2,1,3],[-1,2,4],[-6,1,5] ])
B = np.matrix([ [-2,1,4],[5,0,7],[2,-1,3] ])
C = np.matrix([ [2,3,1,5],[0,6,2,4] ])
D = np.matrix([ [5,7,1],[2,0,3],[1,0,0],[0,5,6] ])
E = np.matrix([ [2,3,5],[-1,6,4],[1,0,6] ])
F = np.matrix([ [0,-1,2],[3,1,2],[-7,3,5] ])
G = np.matrix([ [1,-1,2],[3,5,6],[2,4,-1] ])
H = np.matrix([ [2],[1],[3] ])

#Realizamos nuestras operaciones
AB = (5*A) - (3*B)
CD = C*D
EF = E*F
GH = G*H

#Imprimimos los resultados
print(f"\nProblema 21) \nMatriz A: \n{A} \nMatriz B: \n{B} \nEl resultado de realizar la operación 5A - 3B es igual a: \n{AB}\n")
print(f"\nProblema 24) \nMatriz C: \n{C} \nMatriz D: \n{D} \nEl producto CD es igual a: \n{CD}\n")
print(f"\nProblema 25) \nMatriz E: \n{E} \nMatriz F: \n{F} \nEl producto EF es igual a: \n{EF}\n")
print(f"\nProblema 28) \nMatriz G: \n{G} \nMatriz H: \n{H} \nEl producto GH es igual a: \n{GH}")