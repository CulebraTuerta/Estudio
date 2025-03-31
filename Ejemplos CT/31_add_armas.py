# Hacer un programa que permita añadir un numero de armas seleccionado por el usuario al arsenal de "Personaje" y mostrarlas

arsenal=[]
cantidad=int(input("Cuantas armas quieres agregar? "))
contador=0

while contador <cantidad:
    arma = input(f"Añade arma nº{contador+1} al aresenal: ")
    arsenal.append(arma)    
    contador+=1

print("\nHas finalizado el agregar armas")
print(f"Tu arsenal incluye: {arsenal}")