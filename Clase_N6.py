# -*- coding: utf-8 -*-
"""
Editor de Spyder

"""
#Opcion 1

color = input("Color semáforo: ").upper()

if color == "ROJO":
    print("Detenerse")
else:
    if color == "AMARILLO":
        print("Cruzar con precaución")
    else:
        if color == "VERDE":
            print("Continuar")
        else:
            print("Color no válido")


#opción 2
            
color = input("Color semáforo: ").upper()

if color == "ROJO":
    print("Detenerse")
elif color == "AMARILLO":
    print("Cruzar con precaución")
elif color == "VERDE":
    print("Continuar")
else:
    print("Color no válido")