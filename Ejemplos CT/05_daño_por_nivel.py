#5. En un video juego el personaje principal recibe un aumento de daño del 10% con cada nivel que sube. Recibir por teclado el nivel y el daño base del personaje y mostrar cual seria 
#   el daño final

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


