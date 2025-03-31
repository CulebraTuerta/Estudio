# Hacer una función que permita llenar una lista de tamaño ingresado por el usuario y otra que permita recorrer y mostrar una o más listas.

def llenar(tamaño):
    lista = [0]*tamaño  # creamos la lista llena de ceros para poder tener el largo, de lo contrario da error.
    for i in range(tamaño):
        lista[i]=input(f"Valor #{i+1}: ")
    return lista

def mostrar(*args):
    for lista in args:
        print(lista)

    
a=llenar(3)     # Creo 2 listas, donde me preguntaran el relleno despues,
b=llenar(2)     # Ahora solo especificamos el largo de cada lista.
mostrar(a,b)    # Mando a que se muestren las listas
