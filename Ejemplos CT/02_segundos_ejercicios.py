#1. Para comprar una pocion roja, Link necesita  30 rupias. Hacer un programa que permita ingresar un numero de rupias 
#   y mostrar si puede o no comprar la pocion, en caso de que no, decir cuantas rupias le faltan.

# rupias = int(input("Cuantas Rupias tienes?: "))
# if rupias >= 30:
#     print("Puedes obtener una Pocion")
#     compra = input("Quieres comprar una? (yes/no)")
#     if compra == "yes":
#         print("Has obtenido una Pocion")
#         print(f"Rupias restantes: {rupias-30}")
#     elif compra== "no":
#         print("No has comprado nada")
#     else:
#         print("No entiendo lo que dices, sal de mi negocio!")
# else:
#     print(f"No tienes Rupias suficientes, te faltan {30-rupias}")

#2. Hacer un programa que permita ingresar el nombre de un estudiante y 3 notas con valor de 0 a 5. 
#   Calcular promedio y si es mayor o igual a 3 mostrar "Aprobado", de lo contrario "Reprobado"

# nombre =input("Ingrese nombre de estudiante: ")
# nota1 = int(input("Ingrese Nota 1: "))
# nota2 = int(input("Ingrese Nota 2: "))
# nota3 = int(input("Ingrese Nota 3: "))

# promedio = (nota1+nota2+nota3)/3
# if promedio >=3:
#     print(f"Aprobado con promedio {promedio}")
# else: 
#     print(f"Reprobado con nota {promedio}")

#3. Realizar un programa que permita ingrear una contraseña de por lo menos 7 caracteres. 
#   Luego preguntarla y verificar si es correcta o no , en caso de no serlo, seguir preguntando hasta que se ingrese la correcta.  

# continuar=True
# pswrd= input("Cree su contraseña de al menos 7 caracteres: ")
# if len(pswrd)<7:
#     print("Contraseña no cumple con estandares, se cierra programa")
# else:
#     while continuar:
#         contra = input("Ingrese su contraseña: ")
#         if contra != pswrd:
#             print("Contraseña incorrecta")
#         else:
#             continuar=False
#     print("Contraseña correcta, bienvenido")

#4. Mostrar en pantalla los primeros N terminos de la serie de Fibonacci que comienza en 0 y 1, N lo ingresa el usuario.

a=0
b=1
siguiente=0
numero= int(input("Ingrese la longitud de la serie de Fibonacci que desea ver"))
print(a)
print(b)
for i in range(2,numero):
   siguiente= a+b
   print(siguiente)
   a=b
   b=siguiente
   
#5. Crear un menu que permita: 
#   a. Crear un personaje, preguntando Nombre, Tipo, Atributos
#   b. Mostrar el personaje
#   c. Eliminar el personaje
#   d. Salir

# Lista_personajes = []
# continuar=True

# def creacion_personaje():
#     nombre=input("Ingrese el Nombre del personaje: ")
#     tipo=input("Ingrese Raza para el personaje: ")
#     clase=input("Seleccionar Clase: ")
#     agregar_personaje(nombre)

# def agregar_personaje(n):
#     Lista_personajes.insert(0,n)

# while continuar:

#     print("-------------------------")
#     print("Menu de personajes")
#     print("1. Crear un personaje")
#     print("2. Mostrar personajes")
#     print("3. Eliminar un personaje")
#     print("4. Salir")
#     entrada= int(input(""))

#     if entrada==1:
#         creacion_personaje()
#     elif entrada==2:
#         print(Lista_personajes)
#     elif entrada==3:
#         print("Seleccione un personaje a eliminar")
#         #LISTAR LOS PERSONAJES Y SELECCIONAR EL NUMERO PARA ELIMINAR.
#     elif entrada==4:
#         print("Programa finalizado")
#         continuar=False
#     else:
#         print("Opcion no valida")