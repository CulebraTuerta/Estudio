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
        daño_a_jugador=ene["damage"]*ene["arma"]-jug["defensa"]
        daño_a_enemigo=jug["damage"]*jug["arma"]-ene["defensa"]

        if daño_a_enemigo<=0:   # esto lo pusimos porque cuando el enemigo hacia daño negativo, se sumaba a la vida del jugador...
            daño_a_enemigo=0
        elif daño_a_jugador<=0:
            daño_a_jugador=0

        jug["vida"]-=daño_a_jugador
        ene["vida"]-=daño_a_enemigo

        if jug["vida"]<=0:      # con esto hacemos que si la vida baja de cero, entonces que sea cero...
            jug["vida"]=0
        elif ene["vida"]<=0:
            ene["vida"]=0

        print(f"\n{jug["nombre"]} hizo un daño de {daño_a_enemigo} y dejo a {ene["nombre"]} con {ene["vida"]} de vida")
        print(f"{ene["nombre"]} hizo un daño de {daño_a_jugador} y dejo a {jug["nombre"]} con {jug["vida"]} de vida")
        
        if ene["vida"] <= 0:
            print(f"\nHa muerto {ene["nombre"]}")
            return jug["nombre"]
        elif jug["vida"] <= 0:
            print(f"\nHa muerto {jug["nombre"]}")
            return ene["nombre"]
    

jugador=crear_personaje("Tutazon",100,20,2,20)
enemigo=crear_personaje("Slime",60,30,1,5)

ganador=calcular_enfrentamiento(jugador,enemigo)
print(f"El ganador fue {ganador}")
