# Haremos el gorro seleccionador de harry potter y veremos que casa saca mas puntos

g = 0
r = 0
h = 0
s = 0

print("P1. Que te gusta mas, el amanecer o cuando oscurece?")
print("   1) El amanecer")
print("   2) Al oscurecer")
a = int(input(""))

if a == 1:
  g=g+1
  r=r+1
elif a == 2:
  h=h+1
  s=s+1

print("P2. Si me muero, quiero que la gente me recuerde como")
print("   1) El Bueno")
print("   2) El Grande")
print("   3) El Sabio")
print("   4) El Atrevido")
b = int(input(""))

if b == 1:
  h=h+2
elif b == 2:
  s=s+2
elif b == 3:
  r=r+2
elif b == 4:
  g=g+2


print("P3. Que instrumento le da mas placer a tu oido?")
print("   1) El Violin")
print("   2) La Trompeta")
print("   3) El Piano")
print("   4) El Tambor")
c = int(input(""))

if c == 1:
  s=s+4
elif c == 2:
  h=h+4
elif c == 3:
  r=r+4
elif c == 4:
  g=g+4

print("")
print("Haz sido seleccionado para la casa de....", end="")
casa = max(g,r,h,s)
if g==casa:
  print("Griffindor!!")
elif r==casa:
  print("Ravenclaw!!")
elif h==casa:
  print("Hufflepuff!!")
elif s==casa:
  print("Slytherin!!")

print("")
print("Cada casa tiene los siguientes puntajes")
print("Griffindor: ",g)
print("Ravenclaw: ",r)
print("Hufflepuff: ",h)
print("Slytherin: ",s)