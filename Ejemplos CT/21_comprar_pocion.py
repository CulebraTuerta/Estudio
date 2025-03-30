#6. Para comprar una pocion roja, Link necesita  30 rupias. Hacer un programa que permita ingresar un numero de rupias 
#   y mostrar si puede o no comprar la pocion, en caso de que no, decir cuantas rupias le faltan.

rupias = int(input("Cuantas Rupias tienes?: "))
if rupias >= 30:
    print("Puedes obtener una Pocion")
    compra = input("Quieres comprar una? (yes/no)")
    if compra == "yes":
        print("Has obtenido una Pocion")
        print(f"Rupias restantes: {rupias-30}")
    elif compra== "no":
        print("No has comprado nada")
    else:
        print("No entiendo lo que dices, sal de mi negocio!")
else:
    print(f"No tienes Rupias suficientes, te faltan {30-rupias}")
