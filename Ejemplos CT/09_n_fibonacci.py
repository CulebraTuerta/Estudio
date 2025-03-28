#9. Mostrar en pantalla los primeros N terminos de la serie de Fibonacci que comienza en 0 y 1, N lo ingresa el usuario.

a=0
b=1
siguiente=0
numero= int(input("Ingrese la longitud de la serie de Fibonacci que desea ver"))
print(a)
print(b)
for i in range(2,numero):
   siguiente= a+b
   print(siguiente)
   a=b
   b=siguiente
   
