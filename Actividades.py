# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:46:23 2022

@author: Laura Juliana Serrano García - MaKeajse
"""

"""
1. Escriba un programa que pida dos números enteros y que calcule su división, 
escribiendo si la división es exacta o no.
"""
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

division = round(num1 / num2,2)

modulo = num1 % num2

if modulo == 0:
    rta = "División Exacta"
else:
    rta = "División NO exacta"

print(f"División {division} y fue una {rta}")


"""
2. Mejore el programa anterior haciendo que tenga en cuenta que no se puede 
dividir por cero.
"""

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num2 > 0:
    division = round(num1 / num2,2)
    
    modulo = num1 % num2
    
    if modulo == 0:
        rta = "División Exacta"
    else:
        rta = "División NO exacta"
    
    print(f"División {division} y fue una {rta}")

else:
    print("No se puede dividir por cero")
    

"""
3. Escriba un programa que pida dos números y que conteste cuál es el menor 
y cuál el mayor o que escriba que son iguales (mostrando los números).
"""

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num1 > num2:
    print(f"De los números")
