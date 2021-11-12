""""
"Plantilla" de código para realizar cáculos con matrices
Autor MARH
05.11.2021

Funciones:

DETA=np.linalg.det(A)#Determinante
INVA=linalg.inv(A)#Cálculo de la inversa
SXA=np.linalg.solve(A,SOLA)#Resolver sistema de ecuaciones
TA=np.transpose(A)#Transpone A
"""

import numpy as np #Importamos la librería numpy para realizar cálculos entre matrices.
from numpy import linalg #Esto nos permite hallar los determinantes de las matrices.

#Definimos la o las matrices
A=np.matrix([ [2,0],[0,-2] ])#Matriz A

#Imprimimos resultados
print(INVG)#Imprimir resultado