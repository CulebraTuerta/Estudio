#4. Recibir un numero de tres cifras y mostrar sus digitos del primero al ultimo

# Ejercicio 4
numero_de_tres=str(input("Ingresa un numero de 3 cifras:"))
if len(numero_de_tres)!=3:
    print("El numero ingresado no cumple las caracteristicas")
else:
    print(numero_de_tres[0],",",numero_de_tres[1],",",numero_de_tres[2])

