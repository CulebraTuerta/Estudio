# Almacenar 10 numeros enteros en una lista, determinar los numeros terminados en 5 y su posicion en la lista. 

lista=[]

while len(lista)<10:
    nuevo_numero=int(input("Tirate un numero: "))
    lista.append(nuevo_numero)

for pos,i in enumerate(lista): 
    if i%5 == 0:
        if i%10==0:
            print(f"El numero {i} es divisible por 5, pero no termina en 5")
        else:
            print(f"El numero {i} termina en 5 y esta en la posicion {pos+1}")
    else:
        print(f"El numero {i} no termina en 5")