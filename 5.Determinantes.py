""" 
Este programa de Python permite hallar el determinante de una matriz.
Creado el 31 de octubre del 2021
Autor MARH 
"""

import numpy as np #Importamos la librería numpy para realizar cálculos entre matrices.
#Si muestra un error, instalar numpy desde su dispositivo, en su terminal agregar el comando "pip install numpy"

#Definimos las matrices
A = np.matrix([ [1,-1,2],[3,4,2],[-2,3,4] ]) 
B = np.matrix([ [1,-1,2,3],[4,0,2,5],[-1,2,3,7],[5,1,0,4] ])

#Calculamos los determinantes
DETA = np.linalg.det(A)
DETB = np.linalg.det(B)

#Imprimimos los resultados
print(f"Problema 6) En la matriz A: \n{A} \nSu determinante es igual a {DETA}\n")
print(f"Problema 9) En la matriz A: \n{B} \nSu determinante es igual a {DETB}\n")