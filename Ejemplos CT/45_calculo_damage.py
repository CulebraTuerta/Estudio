# Hacer una función que permita calcular el daño recibido por un jugador al luchar con un enemigo, así como el daño que recibirá el enemigo. El daño deberá ser calculado de la siguiente forma:
# Daño = (Daño base * Multiplicador de arma) - Defensa
# Mostrar el daño realizado por el jugador y el enemigo. Si alguno de los dos muere, decir quién ganó el combate.

# Simular hasta morir

def crear_personaje(n,v,d,a,df):
    personaje = {       
        "nombre": n,
        "vida": v,
        "damage": d,
        "arma": a,
        "defensa": df
    }
    return personaje

def calcular_enfrentamiento(jug,ene):
    while jug["vida"] >0 and ene["vida"]>0:
        damage_jugador=ene["damage"]*ene["arma"]-jug["defensa"]
        damage_enemigo=jug["damage"]*jug["arma"]-ene["defensa"]

        jug["vida"]-=damage_jugador
        ene["vida"]-=damage_enemigo

        print(f"El jugador hizo un daño de {damage_enemigo} y dejo al enemigo con {ene["vida"]} de vida")
        print(f"El enemigo hizo un daño de {damage_jugador} y dejo al jugador con {jug["vida"]} de vida")
        
        if ene["vida"] <= 0:
            print(f"Ha muerto {ene["nombre"]}")
            return jug["nombre"]
        elif jug["vida"] <= 0:
            print(f"Ha muerto {jug["nombre"]}")
            return ene["nombre"]
    

jugador=crear_personaje("Tutazon",100,30,2,20)
enemigo=crear_personaje("Slime",50,30,1,40)

ganador=calcular_enfrentamiento(jugador,enemigo)
print(f"El ganador fue {ganador}")
