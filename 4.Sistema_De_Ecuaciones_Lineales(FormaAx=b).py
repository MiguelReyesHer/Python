""" 
Este programa de Python permite hallar las soluciones de un sistema de ecuaciones con la forma Ax=b.
Creado el 31 de octubre del 2021
Equipo: Mafia del poder 2.0
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
A = np.matrix([ [1,-3],[2,2] ]) #Matriz de coeficientes
SOLA = np.matrix([ [4],[3] ]) #Vector solución "b"
B = np.matrix([ [1,2,0],[2,1,-1],[3,1,1] ])
SOLB = np.matrix([ [3],[-1],[7] ])

#Se resuelve el sistema de ecuaciones con np.linalg.solve(MatrizCoeficientes,VectorSolución"b")
#Cuando el sistema es incosistente, la terminal marcará un error
XA = np.linalg.solve(A,SOLA)
XB = np.linalg.solve(B,SOLB)

#Se imprimen los resultados
print(f"Problema 45) El sistema de ecuaciones se cumple con los valores: \n{XA}\n")
print(f"Problema 46) El sistema de ecuaciones se cumple con los valores: \n{XB}\n")