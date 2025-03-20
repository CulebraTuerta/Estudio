import random

num = random.randint(1, 9)
pregunta = str(input("Pregunta: "))

print("Respuesta de la Bola Mágica: ", end="")  # "Respuesta de la Bola Mágica"

if num == 1:
    print("Sí, de más po' weón")  
elif num == 2:
    print("Altiro conchetumare")  
elif num == 3:
    print("Claramente, saco wea")  
elif num == 4:
    print("Ni puta idea, pregúntame de nuevo")  
elif num == 5:
    print("Puta wn, pregúntame después, ahora no estoy pa tus weas")  
elif num == 6:
    print("Mejor no te digo na, pa que no te hagai cagar solito")  
elif num == 7:
    print("Mmm... mis fuentes dicen que nica, cagaste")  
elif num == 8:
    print("Compadre, te vai a ir a la B")  
else:
    print("Ni cagando, compare, ni en un millón de años")  
