import random as ra
import time

print("="*40)
print(" *** Juego de la mente más rápida *** ")
print("="*40)

num1 = ra.randint(1,100)
total = ra.randint(1,100)

num2 = total - num1

print("""\nDebe escribir cuál es el número que 
falta en el menor tiempo posible \n""")
print(f"{total} = {num1} + ??")

inicio = time.time()
num3 = int(input("El número es: "))

fin= time.time()

print(f"\nTe demoraste: {round(fin-inicio,2)} segundos")
print(f"La respuesta es: {num3==num2}, el número faltante era {num2}\n")