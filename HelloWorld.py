"""
Autor MARH - 25/08/2021 - primer código en Phyton.
Código que genera un número random en una lista para que tú lo adivines
"""

import random

#Se añade el número randon a una lista vacía
lista = []
lista.append(random.randrange(1,10))

#Escribe tu respuesta
nombre = input("Hola mundo\n¿Cómo te llamas? ")
respuesta = input(f"{nombre} Adivina en qué número del 1 al 10 estoy pensando: ")
turespuesta = int(respuesta)

#Muestra el resultado
if turespuesta in lista:
    print("Tuviste mucha suerte, has ganado")
else:
    print("Mala suerte, vuelve a intentarlo")