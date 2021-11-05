""" 
Este programa de Python permite hallar las soluciones de un sistema de ecuaciones.
Creado el 31 de octubre del 2021
Autor MARH 
"""

import numpy as np #Importamos la librería numpy para realizar cálculos entre matrices.
#Si muestra un error, instalar numpy desde su dispositivo, en su terminal agregar el comando "pip install numpy"

"""Transformamos el sistema de ecuaciones en su forma Ax=b
 
 Ejemplo: si tenemos el sistema:
 2x + 3y + 4z = 0
    - y  + 5z = 3

Separamos los coeficientes, las variables y el vector solución en diferentes matrices o vectores, según sea el caso, cumpliendo la forma Ax=b

Siguiendo el ejemplo anterior:
Matriz de coeficientes: ([[2,3,4],[0,-1,5]])
Vector de variables: ([x,y,z])
Vector solución: ([0,3])

En este programa únicamente utilizaremos las matrices de coeficientes y el vector solución para hallar los valores que satisfacen el sistema
"""

#Definimos nuestas matrices y vectores solución
A = np.matrix([ [3,6],[-2,3] ]) #Matriz de coeficientes
SOLA = np.matrix([ [9],[4] ]) #Vector solución "b"
B = np.matrix([ [3,-6],[-2,4] ])
SOLB = np.matrix([ [9],[6] ])
C = np.matrix([ [1,1,1],[2,-1,2],[-3,2,3] ])
SOLC = np.matrix([ [2],[4],[8] ])
D = np.matrix([ [1,1,1,1],[2,-3,-1,4],[-2,4,1,-2],[5,-1,2,1] ])
SOLD = np.matrix([ [4],[7],[1],[-1] ])
E = np.matrix([ [2,-1,6],[6,5,18],[4,4,-3] ])
SOLE = np.matrix([ [0],[0],[0] ])

#Se resuelve el sistema de ecuaciones con np.linalg.solve(MatrizCoeficientes,VectorSolución"b")
#Cuando el sistema es incosistente, la terminal marcará un error
XA = np.linalg.solve(A,SOLA)
#XB = np.linalg.solve(B,SOLB)
XC = np.linalg.solve(C,SOLC)
XD = np.linalg.solve(D,SOLD)
XE = np.linalg.solve(E,SOLE)

#Se imprimen los resultados
print(f"Problema 1) El sistema de ecuaciones se cumple con los valores: \n{XA}\n")
#print(f"Problema 4, el sistema de ecuaciones se cumple con los valores: \n{XB}\n")
print("Problema 4) El sistema es inconsistente, no hay soluciones que cumplan al sistema en sí\n")
print(f"Problema 5) El sistema de ecuaciones se cumple con los valores: \n{XC}\n")
print(f"Problema 15) El sistema de ecuaciones se cumple con los valores: \n{XD}\n")
print(f"Problema 18) El sistema de ecuaciones se cumple con los valores: \n{XE}\n")

"""
Se han desabilitado las operaciones con el sistema de ecuaciones "B" haciéndolos comentarios debido a que el sistema es incosistente, 
cuando es inconsistente marca un error en la terminal, impidiendo mostrar las demás soluciones
"""