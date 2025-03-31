# Hacer una función para crear personajes con los siguientes atributos:
# Nombre, vida, daño base, arma (multiplicador de daño) y defensa.

def crear_personaje(n,v,d,a,df):
    personaje = {       # Esto es un diccionario para guardar al personaje con sus caracteristicas
        "nombre": n,
        "vida": v,
        "damage": d,
        "arma": a,
        "defensa": df
    }
    return personaje

nombre=input("Ingrese el Nombre del personaje: ")
vida=int(input("Ingrese Vida: "))
damage=int(input("Ingrese Daño Base: "))
arma=damage*1.1
defensa=int(input("Ingresar Defensa: "))

personaje1 = crear_personaje(nombre,vida,damage,arma,defensa)

print(personaje1)