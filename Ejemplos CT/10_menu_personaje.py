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
    personaje = {       # Esto es un diccionario para guardar al personaje con sus caracteristicas
        "nombre": nombre,
        "tipo": tipo,
        "clase": clase,
    }
    Lista_personajes.insert(0,personaje) # Aqui se guarda con todos sus datos adjuntos


while continuar:

    print("-------------------------")
    print("Menu de personajes")
    print("1. Crear un personaje")
    print("2. Mostrar personajes")
    print("3. Eliminar un personaje")
    print("4. Salir")
    print("-------------------------")
    entrada= int(input(""))

    # Autoexplicativo
    if entrada==1:
        creacion_personaje() 

    # Mostrar a los personajes
    elif entrada==2:
        print("Lista de personajes:")
        for i, personaje in enumerate(Lista_personajes,start =1): # Esto repasa toda la lista de personajes que existen
            print(f"{i}. {personaje["nombre"]}") # y muestra solo los nombres
        opcion= int(input("Seleccione personaje (cero para cerrar) ")) 
        if opcion > len(Lista_personajes) or opcion < 0:
            print("Error al selecionar personaje")
        elif opcion == 0:
            exit
        else:               # Al personaje indicado se le muestra todas sus caracteristicas
            x=Lista_personajes[opcion-1] 
            print(f"Personaje: {x["nombre"]}")
            print(f"Raza: {x["tipo"]}")
            print(f"Clase: {x["clase"]}")

    # Mismo proceso anterior pero para eliminar algun personaje   
    elif entrada==3:         
        print("Seleccione un personaje a eliminar")
        for i, personaje in enumerate(Lista_personajes,start =1):
            print(f"{i}. {personaje["nombre"]}")
        opcion= int(input(""))
        if opcion > len(Lista_personajes) or opcion <= 0:
            print("Error al selecionar personaje a eliminar")
        else: 
            del Lista_personajes[opcion-1]

    # Autoexplicativo
    elif entrada==4:    
        print("Programa finalizado")
        continuar=False
    else:
        print("Opcion no valida")