# Hacer un programa que permita añadir un numero de armas seleccionado por el usuario al arsenal de "Personaje" y mostrarlas

arsenal=[]
cantidad=int(input("Cuantas armas quieres agregar? "))
contador=0

while contador <cantidad:
    arma = input("Añade una arma al aresenal: ")
    arsenal.append(arma)
    print(f"Tu arsenal incluye: {arsenal}")
    contador+=1

print("Has finalizado el agregar armas")