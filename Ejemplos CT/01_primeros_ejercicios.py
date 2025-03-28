#1. Recibir el nombre del usuario por teclado y mostrar por pantalla "Hola " (nombre)
#2. Realizar un programa que permita leer un numero y mostrar su tabla de multiplicar del 1 al 10
#3. Calcular el resultado de la siguiente operacion matematica: raiz de 45-(3 elevado a 2) todo eso dividido por 2 por 3  y todo eso menos 1
#4. Recibir un numero de tres cifras y mostrar sus digitos del primero al ultimo
#5. En un video juego el personaje principal recibe un aumento de daño del 10% con cada nivel que sube. Recibir por teclado el nivel y el daño base del personaje y mostrar cual seria 
#   el daño final

# Ejercicio 1
# nombre = str(input("Cual es tu nombre?:"))
# print("Hola",nombre,"!!")

# Ejercicio 2
# numero = int(input("Ingresa un numero:"))
# for i in range (1,10,1):
#     print(f"{numero}*{i}={numero*i}")

# Ejercicio 3
# var_sup=(45-(3**2))**(1/2)
# total=(var_sup/6)-1
# print(f"El total es:{total}")

# Ejercicio 4
# numero_de_tres=str(input("Ingresa un numero de 3 cifras:"))
# if len(numero_de_tres)!=3:
#     print("El numero ingresado no cumple las caracteristicas")
# else:
#     print(numero_de_tres[0],",",numero_de_tres[1],",",numero_de_tres[2])

# Ejercicio 5
nivel = int(input("Ingresa el nivel del personaje:"))
damage = int(input("Ingrese el daño base:"))
for i in range(1,5,1):
    damage *=1.1
    print(f"En nivel {i+nivel}, daño: {damage}")

# esto muestra el daño pero con el 10% aplicado en el daño del nivel anterior y no el base, en el caso de un juego
# es mejor considerar juntar todo el daño base y a eso ponerle los multiplicativos de porcentaje de daño. 
# es decir, si de base hago 100, en nivel 5 deberia hacer 150% de daño. Es mas facil calcularlo asi que de la manera
# que propuse yo. 


