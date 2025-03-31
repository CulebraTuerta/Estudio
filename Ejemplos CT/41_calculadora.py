# Realizar una función que permita calcular la tabla de multiplicar de un número hasta el 10, o hasta un valor ingresado por el usuario.

def mostrar_tabla(num,contador=10):
    for i in range (1,contador+1):        
        print(f"{num}*{i}={num*i}")

numero = int(input("Ingresa un numero:"))
contador = int(input("Ingrese largo de tabla (default 10). De lo contrario, ingrese 0"))
if contador!=0:
    mostrar_tabla(numero,contador)
else:
    mostrar_tabla(numero)

