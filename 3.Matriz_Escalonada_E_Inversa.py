""" 
Este programa de Python permite hallar la inversa y la forma escalonada reducida de matrices.
Creado el 31 de octubre del 2021
Autor MARH 
"""

import numpy as np #Importamos la librería numpy para realizar cálculos entre matrices.
from numpy import linalg #Esto nos permite hallar los determinantes de las matrices.
#Si muestra un error, instalar numpy desde su dispositivo, en su terminal agregar el comando "pip install numpy"

#Definimos las matrices que usaremos en todo el probema
A = np.matrix([ [2,3],[-1,4] ])
B = np.matrix([ [-1,2],[2,-4] ])
C = np.matrix([ [3,4],[6,8] ])
D = np.matrix([ [1,2,0],[2,1,-1],[3,1,1] ])

#Imprimimos las matrices de nuestros problemas
print(f"Sean las matrices: \nA: {A}\n\nB: {B}\n\nC: {C}\n\nD: {D}\n")

#Realizamos los cálculos para la matriz A
DETA = np.linalg.det(A) #Calculamos el determinante para saber si tiene inversa o no
if DETA == 0: #Si el det(A) = 0, no existe la inversa
    print(f"Problema 37) La inversa de la matriz A no existe dado que el determinante es igual a cero \ndet(A) = {DETA}\n") #Mostramos el resultado
else: #Si el determinante es diferente a cero, se calcula su inversa
    INVA = linalg.inv(A) #Cálculo de la inversa
    REDA = A*INVA #Para hallar su forma escalonada reducida se multiplica la matriz original con su inversa =  matriz identidad
    print(f"Problema 37) La inversa de la matriz A es: \nA^-1 = {INVA} \nSu forma escalonada reducida es: \n{REDA}\n") #Mostramos el resultado
#Esta estructura se repite para las demás matrices

#Realizamos los cálculos para la matriz B
DETB = np.linalg.det(B) 
if DETB == 0:
    print(f"Problema 38) La inversa de la matriz B no existe dado que el determinante es igual a cero \ndet(B) = {DETB}\n")
else:
    INVB = linalg.inv(B)
    REDB = B*INVB
    print(f"Problema 38) La inversa de la matriz B es: \nB^-1 = {INVB} \nSu forma escalonada reducida es: \n{REDB}\n")

#Realizamos los cálculos para la matriz C
DETC = np.linalg.det(C) 
if DETC == 0:
    print(f"Problema 39) La inversa de la matriz C no existe dado que el determinante es igual a cero \ndet(C) = {DETC}\n")
else:
    INVC = linalg.inv(C)
    REDC = C*INVC
    print(f"Problema 39) La inversa de la matriz C es: \nC^-1 = {INVC} \nSu forma escalonada reducida es: \n{REDC}\n")

#Realizamos los cálculos para la matriz D
DETD = np.linalg.det(D) 
if DETD == 0:
    print(f"Problema 40) La inversa de la matriz D no existe dado que el determinante es igual a cero \ndet(D) = {DETD}")
else:
    INVD = linalg.inv(D)
    REDD = D*INVD
    print(f"Problema 40) La inversa de la matriz D es: \nD^-1 = {INVD} \nSu forma escalonada reducida es: \n{REDD}")