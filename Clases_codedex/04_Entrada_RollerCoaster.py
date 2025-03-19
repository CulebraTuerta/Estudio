# la idea es preguntar si el qlo es lo suficiente mente alto y si tiene plata y asi puede entrar
# a la montaña rusa cyclone

print ("Requisitos para entrar al Cyclone")
print ("Altura minima: 137 cm")
print ("Creditos: 10")
print ("")

altura = int(input("Introduzca su altura (en cm): "))
creditos = int(input("Introduzca sus creditos actuales: "))

# suficiente alto y tiene moni
# si no es alto pero tiene plata, decir eri shico
# si no tiene plata pero es alto, decir eres pobre
# si no cumple con ninguno de los dos, decir ggwp

if altura >= 137 and creditos >=10:
  print("Disfruta la atraccion")
elif altura < 137 or creditos <10:
  if (altura<137):
    print("No cumple con altura minima")
  else:
    print("No tiene creditos suficientes")
else:
  print("No cumple con ninguno de los requisitos")