##ACTIVIDAD DEL SEMAFORO

""" Manejo de condicionales """

color = input("Ingrese el Color: ").upper()

if color == "ROJO":
    print("Detener")
else:
    if color == "VERDE":
        print("Puede pasar")
    elif color == "AMARILLO":
        print("Cruzar con precaución")
    else:
        print("Color no válido")
