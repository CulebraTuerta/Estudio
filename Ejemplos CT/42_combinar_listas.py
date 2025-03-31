# Realizar una función que permita recibir varias listas y combinarlas.

def combinar(*args):
    for i in args:
        print(i)
        lista_final.append(i)
    return lista_final

lista_final = []

a=[2,4,5]
b=[True,False]
c=["Hola","Puto"]

print(combinar(a+b+c))

# AUN ME QUEDAN DUDAS COMO FUNCIONA, PERO PUEDO COMBINAR LISTAS...