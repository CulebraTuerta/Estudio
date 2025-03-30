# Hacer un programa que muestre al jugador una lista de habilidades por aprender, cada una con un precio en puntos.
# El jugador con una cantaidad de puntos base podra elegir que habilidad aprender la cual deberea ser eliminiada de la lista. 
# mostrar al final las habilidades que faltan por aprender. 

habilidades_aprendidas= []

diccionario_habilidades={       # Esto es un diccionario para habilidades
        "Fuego Volador":"2",
        "Hielo Congelador":"4",
        "Explosion de Mana":"5",
    }

cantidad_puntos = int(input("\nCuantos puntos de habilidad tienes? "))

while diccionario_habilidades:
        
    if cantidad_puntos <2:
        print("No tienes puntos de habilidad suficientes")
        break
    else:
        print("\nHabilidades disponibles: ")
        habilidades = list(diccionario_habilidades.keys()) 
        # Esto convierte las claves del diccionario en una lista llamada habilidades, recordar que las "claves" son la primera info de un diccionario

        for pos,val in enumerate(habilidades,start=1):    # Esto entrega toda la info de las habilidades disponibles y su costo, val es en este caso las "claves"
            print(f"{pos}. {val} (costo {diccionario_habilidades[val]} puntos)")   # ya que esta recorriendo todas las habilidades disponibles.

        opcion=int(input("Que habilidad quieres aprender? "))-1   # con esto estoy identificando la opcion del jugador, la eleccion de habilidad de la lista disponible

        if 0<= opcion < len(habilidades):   # esa opcion tiene que ser menor a los numeros que aparecen en la lista 
            habilidad_seleccionada = habilidades[opcion]    # selecciono el nombre de la habilidad seleccionada, en este caso el valor de la "clave" actual  
            costo = int(diccionario_habilidades[habilidad_seleccionada])    # aqui guardo el valor de la habilidad, este se puede identificar desde el nombre de la clave. 
                                                                            # Recordar que los diccionarios son "keys and values"
            if cantidad_puntos >= costo:  # si tengo los puntos suficientes, entonces....
                habilidades_aprendidas.append(habilidad_seleccionada)   # guardo la habilidad en habilidades aprendidas
                del diccionario_habilidades[habilidad_seleccionada]     # la eliminio del diccionario
                cantidad_puntos -= costo    # resto el costo de mi cantidad de puntos disponibles
                print(f"\nHas aprendido {habilidad_seleccionada}")    
                print(f"Puntos restantes: {cantidad_puntos}")
            else:
                print("\nNo tienes puntos suficientes")
        else:
            print("Esa opcion no existe")


        
        print(f"\nHabilidades aprendidas {habilidades_aprendidas}")

print("\nNo quedan mas habilidades por aprender o no quedan suficientes puntos")
