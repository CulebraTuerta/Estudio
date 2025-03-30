# Recibir n numeros enteros por teclado, añadir a una lista los que sean primos y mostrarlos por pantalla. 

lista= []

def es_primo(num):
    if num==2:
            return True
    else:
        for n in range(2,num):
            if num%n==0:
                print(f"No es primo, {n}, es divisor")
                return False
            else:
                return True
    
while True:
    numero = int(input("Ingresa un número: "))

    if es_primo(numero):
        print(f"{numero} es primo.")
        lista.append(numero)
        print(lista)
    else:
       continue    