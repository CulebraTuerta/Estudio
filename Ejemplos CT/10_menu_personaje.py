#10. Crear un menu que permita: 
#   a. Crear un personaje, preguntando Nombre, Tipo, Atributos
#   b. Mostrar el personaje
#   c. Eliminar el personaje
#   d. Salir

Lista_personajes = []
continuar=True

def creacion_personaje():
    nombre=input("Ingrese el Nombre del personaje: ")
    tipo=input("Ingrese Raza para el personaje: ")
    clase=input("Seleccionar Clase: ")
    agregar_personaje(nombre)

def agregar_personaje(n):
    Lista_personajes.insert(0,n)

while continuar:

    print("-------------------------")
    print("Menu de personajes")
    print("1. Crear un personaje")
    print("2. Mostrar personajes")
    print("3. Eliminar un personaje")
    print("4. Salir")
    entrada= int(input(""))

    if entrada==1:
        creacion_personaje()
    elif entrada==2:
        print(Lista_personajes)
        #SELECCIONAR UN PERSONAJE Y AHI MOSTRAR SUS CARACTERISTICAS.
    elif entrada==3:
        print("Seleccione un personaje a eliminar")
        #LISTAR LOS PERSONAJES Y SELECCIONAR EL NUMERO PARA ELIMINAR.
    elif entrada==4:
        print("Programa finalizado")
        continuar=False
    else:
        print("Opcion no valida")