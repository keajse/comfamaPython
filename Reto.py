# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:03:45 2022

@author: Laura Juliana Serrano García - MaKeajse
"""

"""
RETO CLASE

Realizar el juego de la mente más rápido ingresando
un menú de operaciones.

1. SUMA
2. RESTA
3. MULTIPLICACIÓN
4. DIVISIÓN

"""

import random as ra
import time

print("="*40)
print(" *** Juego de la mente más rápida *** ")
print("="*40)

num1 = ra.randint(1,100)
num2 = ra.randint(1,100)

operacion = int(input("""Ingrese el número de la operación que desea realizar:
    1. SUMA
    2. RESTA
    3. MULTIPLICACIÓN
    4. DIVISIÓN
    
    Su respuesta: """))
    
print("""\nDebe escribir cuál es el número que 
    falta en el menor tiempo posible \n""")

if operacion == 1:

    total = num1 + num2     
    print(f"{num1} + ?? = {total}")
    
    inicio = time.time()
    num3 = int(input("El número es: "))
    
    fin= time.time()
    

elif operacion == 2:
    num1 = ra.randint(100,200)
    num2 = ra.randint(1,100)
    
    total = num1 - num2     
    print(f"{num1} - ?? = {total}")
    
    inicio = time.time()
    num3 = int(input("El número es: "))
    
    fin= time.time()
    
elif operacion == 3:
    
    total = num1 * num2     
    print(f"{num1} * ?? = {total}")
    
    inicio = time.time()
    num3 = int(input("El número es: "))
    
    fin= time.time()
    
elif operacion == 4: 
    num1 = ra.randint(1,100)
    num2 = ra.randint(1,20)
       
    total = round(num1 / num2, 2)
    print(f"{num1} / ?? = {total}")
    
    inicio = time.time()
    num3 = int(input("El número es: "))
    
    fin= time.time()

else:
    print("Operación no válida")
    inicio = time.time()
    fin = time.time()
    num2 = "XXXX"
    

print(f"\nTe demoraste: {round(fin-inicio,2)} segundos")
#print(f"La respuesta es: {num3==num2}")

if num3 == num2:
    print("RESPUESTA CORRECTA")
    
else:
    print(f"RESPUESTA INCORRECTA, el valor faltante es: {num2}")

